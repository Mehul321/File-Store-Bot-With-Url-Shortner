# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

class Config(object):
  # --- TERI DETAILS (Hardcoded for GitHub) ---
  API_ID = int(os.environ.get("API_ID", "26386777"))
  API_HASH = os.environ.get("API_HASH", "ee7bbb1078fa4aaf4c1b6e9cfeec3ca1")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8398492174:AAH9s6x3YYKVTMTKsceE-LAzSwJPr-B1CRg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "BlackDevilking_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003486068610"))
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "910090161"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mehulrathod8514:IpEFuQmV5zFUWd0B@cluster0.91zmh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  
  # Shortener Settings
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "kingshortx.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "C62b3eb6a2fd5fa64d03dc8e2d06d616f2fc2be1") 
  
  # --- NEW: Automatic Batching Settings ---
  # Bot 30 seconds wait karega saari files collect karne ke liye
  BATCH_TIME = int(os.environ.get("BATCH_TIME", 30)) 
  # ----------------------------------------

  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003486068610"))
  
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split() if x.strip())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split() if x.strip()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot with Auto-Batching.
Send me multiple files, wait for {BATCH_TIME} seconds, and get a single link!

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
I am Super noob Please Support My Hard Work.
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

**Auto-Batching is ON!**
📢 Just send me all your files. I will wait for 30 seconds and give you a single link. No need to use /batch command!
"""
  
