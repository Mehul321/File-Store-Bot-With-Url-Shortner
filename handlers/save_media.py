import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

# Temporary storage for automatic batching
USER_BATCHES = {}

def generate_random_alphanumeric():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))

def get_short(url):
    try:
        rget = requests.get(f"https://{Config.SHORTLINK_URL}/api?api={Config.SHORTLINK_API}&url={url}&alias={generate_random_alphanumeric()}")
        rjson = rget.json()
        if rjson.get("status") == "success" or rget.status_code == 200:
            return rjson["shortenedUrl"]
        return url
    except:
        return url

async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        await asyncio.sleep(sl.value)
        return await forward_to_channel(bot, message, editable)

async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        # Getting actual message objects from the IDs we stored
        for msg_id in message_ids:
            try:
                msg = await bot.get_messages(chat_id=editable.chat.id, message_ids=msg_id)
                sent_message = await forward_to_channel(bot, msg, editable)
                if sent_message:
                    message_ids_str += f"{str(sent_message.id)} "
                await asyncio.sleep(1) # Chota delay for safety
            except:
                continue
        
        if not message_ids_str:
            return await editable.edit("Failed to store files.")

        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str.strip(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Delete Batch", callback_data="closeMessage")]])
        )
        
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=VJBotz_{str_to_b64(str(SaveMessage.id))}"
        short_link = get_short(share_link)
        
        await editable.edit(
            f"**Your Batch is Ready!**\n\nTotal Files: `{len(message_ids)}` \nLink: <code>{short_link}</code>",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Original Link", url=share_link),
                InlineKeyboardButton("Short Link", url=short_link)
            ]]),
            disable_web_page_preview=True
        )
    except Exception as err:
        await editable.edit(f"Error: {err}")

async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    user_id = message.from_user.id
    
    # Check if user already has a batch starting
    if user_id not in USER_BATCHES:
        USER_BATCHES[user_id] = [message.id]
        # Start the timer for 30 seconds (or Config.BATCH_TIME)
        await editable.edit(f"**Batching Started...**\n\nSending more files? I'll wait for {Config.BATCH_TIME} seconds.")
        
        await asyncio.sleep(Config.BATCH_TIME)
        
        # After 30 seconds, process all collected IDs
        final_ids = USER_BATCHES.pop(user_id)
        if len(final_ids) == 1:
            # Single file logic
            await process_single_file(bot, editable, message)
        else:
            # Batch logic
            await save_batch_media_in_channel(bot, editable, final_ids)
    else:
        # User is already in a batch, just add the new message ID
        USER_BATCHES[user_id].append(message.id)
        await editable.edit(f"**Added to Batch!**\n\nTotal files collected: `{len(USER_BATCHES[user_id])}`\nWaiting for more...")

async def process_single_file(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=VJBotz_{str_to_b64(str(forwarded_msg.id))}"
        short_link = get_short(share_link)
        await editable.edit(
            f"**File Stored!**\n\nLink: <code>{short_link}</code>",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Original Link", url=share_link),
                InlineKeyboardButton("Short Link", url=short_link)
            ]]),
            disable_web_page_preview=True
        )
    except Exception as err:
        await editable.edit(f"Error: {err}")
