import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# ==================( BOT CORE )================== #
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8545421376:AAFzFdh_7_sywo7_KbiJ29gYKux4ALBckCA")
APP_ID = int(os.environ.get("APP_ID", "33882007"))
API_HASH = os.environ.get("API_HASH", "799677df02c75c218e83f74a70c1eef9")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003734749769")
OWNER = os.environ.get("OWNER", "SKANIME04")
OWNER_ID = int(os.environ.get("OWNER_ID", "7033830081"))

PORT = os.environ.get("PORT", "8001")
BASE_URL = os.environ.get("BASE_URL", "https://infinity-file.onrender.com/")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Root66:root@cluster0.aoo8mij.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/SKANIME04")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/FkgGQYby/welcome.png")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/FkgGQYby/welcome.png")

# ==================( SHORTLINK )================== #
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://arolink.com")
SHORTLINK_API = os.environ.get("AROLINK_API", "b14079f8742020af56a76a9cd83ef3b0775ca78b")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/H0W_2_USE/12")
SHORT_MSG = "<b>⛩ ʏᴇ ʀᴀʜᴀ ᴛᴇʀᴀ ᴀɴɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ — ᴘᴇʜʟᴇ ᴛᴜᴛᴏʀɪᴀʟ ᴅᴇᴋʜ ʟᴇ ꜱᴇɴᴘᴀɪ!</b>"
SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")

# ==================( TEXTS )================== #
HELP_TXT = """<b><blockquote>⛩ 𝗔𝗡𝗜𝗠𝗘 𝗙𝗜𝗟𝗘 𝗦𝗧𝗢𝗥𝗘 𝗕𝗢𝗧 — @CARTOONFUNNY04

❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs
├ /start : ꜱᴛᴀʀᴛ ᴛʜᴇ ᴀɴɪᴍᴇ ᴊᴏᴜʀɴᴇʏ
├ /about : ʙᴏᴛ ᴋᴀ ɪɴꜰᴏ
└ /help : ʜᴇʟᴘ ᴍᴇɴᴜ

🎌 ʟɪɴᴋ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴏ → ʙᴏᴛ ꜱᴛᴀʀᴛ ᴋᴀʀᴏ → ᴅᴏɴᴏ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴋᴀʀᴏ → ᴀɴɪᴍᴇ ʟᴇ ᴊᴀᴏ!

🛠 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href="https://t.me/SKANIME04">CARTOONFUNNY04</a></blockquote></b>"""

ABOUT_TXT = """<b><blockquote>
🏴‍☠️ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴀɴᴅ ᴀɴɪᴍᴇ ᴜɴɪᴠᴇʀꜱᴇ
🎌 ᴄʀᴇᴀᴛᴏʀ : <a href="https://t.me/CARTOONFUNNY04">CARTOONFUNNY04</a>
📺 ᴍᴀɪɴ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/CARTOONFUNNY04">CARTOONFUNNY04</a>
🔥 ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ • ꜱᴜʙʙᴇᴅ • ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇꜱ
⚡ ɴᴇᴡ ᴇᴘɪꜱᴏᴅᴇꜱ ᴜᴘᴅᴀᴛᴇᴅ ʀᴇɢᴜʟᴀʀʟʏ
🛠 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : <a href="https://t.me/SKANIME04">SKANIME04</a>
</blockquote></b>"""

START_MSG = os.environ.get("START_MESSAGE", """<b>⛩ ᴋᴏɴɴɪᴄʜɪᴡᴀ {mention}!

<blockquote>🎌 ᴍᴀɪɴ ʜᴜ ᴀɴɪᴍᴇ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ — ᴀɴɪᴍᴇ ᴇᴘɪꜱᴏᴅᴇꜱ, ᴍᴏᴠɪᴇꜱ ᴀᴜʀ ʙᴀᴛᴄʜᴇꜱ ᴋᴏ ꜱᴇᴄʀᴇᴛ ᴠᴀᴜʟᴛ ᴍᴇɪɴ ꜱᴛᴏʀᴇ ᴋᴀʀᴋᴇ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ ʙᴀɴᴀᴛᴀ ʜᴜ.</blockquote></b>""")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """<b>⛩ ᴏʜᴀʏᴏ {mention}!

<blockquote>🎌 ᴀɴɪᴍᴇ ꜰɪʟᴇ ᴜɴʟᴏᴄᴋ ᴋᴀʀɴᴇ ᴋᴇ ʟɪʏᴇ ʜᴀᴍᴀʀᴇ ᴄʜᴀɴɴᴇʟꜱ ᴊᴏɪɴ ᴋᴀʀᴏ, ᴘʜɪʀ ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ ᴅᴀʙᴀᴏ.</blockquote></b>""")

CMD_TXT = """<blockquote><b>⛩ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs (ᴀɴɪᴍᴇ ʜQ):</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs ʟɪsᴛ
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ᴀᴅᴍɪɴs ʟɪsᴛ
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴs
<b>›› /delreq :</b> ʀᴇᴍᴏᴠᴇ ʟᴇғᴛᴏᴠᴇʀ ɴᴏɴ-ʀᴇǫᴜᴇsᴛ ᴜsᴇʀs
"""

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>⛩ ᴀɴɪᴍᴇ ʙʏ @CARTOONFUNNY04</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>⛩ ᴀɴɪᴍᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ</b>\n{uptime}"
USER_REPLY_TEXT = "🎌 ꜱᴇɴᴘᴀɪ, ꜱᴇᴇᴅʜᴀ ʙᴀᴀᴛ ᴍᴀᴛ ᴋᴀʀ — /start ᴅᴀʙᴀᴏ!"

# ==================( BUY PREMIUM )================== #
OWNER_TAG = os.environ.get("OWNER_TAG", "SKANIME04")
UPI_ID = os.environ.get("UPI_ID", "20213904@axl")
QR_PIC = os.environ.get("QR_PIC", "https://i.ibb.co/35QF8QMJ/QR.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "t.me/SKANIME04")

PRICE1 = os.environ.get("PRICE1", "0 rs")
PRICE2 = os.environ.get("PRICE2", "60 rs")
PRICE3 = os.environ.get("PRICE3", "150 rs")
PRICE4 = os.environ.get("PRICE4", "280 rs")
PRICE5 = os.environ.get("PRICE5", "550 rs")

# ==================( LOGGING )================== #
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
