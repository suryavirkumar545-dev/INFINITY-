import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# ---- Bot credentials (GitHub push se pehle env vars me daalo) ----
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID       = int(os.environ.get("APP_ID", "0"))
API_HASH     = os.environ.get("API_HASH", "")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003734749769"))   # DB channel
OWNER      = os.environ.get("OWNER", "SKANIME04")                 # owner username (no @)
OWNER_ID   = int(os.environ.get("OWNER_ID", "7032769404"))

PORT     = os.environ.get("PORT", "8001")
BASE_URL = os.environ.get("BASE_URL", "https://infinity-op8p.onrender.com/")

DB_URI  = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "FilestoreDB")

FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))
BAN_SUPPORT      = os.environ.get("BAN_SUPPORT", "https://t.me/SKANIME04")   # contact support
TG_BOT_WORKERS   = int(os.environ.get("TG_BOT_WORKERS", "200"))

# SK ANIME FILE STORE — 5 random start banners (16:9)
BANNER_BASE = "https://project--c5b9624b-32d2-48f1-82aa-208313351e70-dev.lovable.app/thumbs"
START_PICS = os.environ.get("START_PICS", " ".join(f"{BANNER_BASE}/sk-{i}.jpg" for i in range(1, 6))).split()
START_PIC = START_PICS[0]
FORCE_PIC = os.environ.get("FORCE_PIC", START_PICS[1])

# Force-Subscribe main channel
FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL", "@CARTOONFUNNY04")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
TUT_VID       = os.environ.get("TUT_VID", "https://t.me/CARTOONFUNNY04")
SHORT_MSG     = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"
SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")

HELP_TXT  = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @CARTOONFUNNY04\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/SKANIME04>@SKANIME04</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ʙᴏᴛ : SK ANIME FILE STORE\n◈ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/CARTOONFUNNY04>@CARTOONFUNNY04</a>\n◈ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/CARTOONFUNNY04>@CARTOONFUNNY04</a>\n◈ sᴜᴘᴘᴏʀᴛ : <a href=https://t.me/SKANIME04>@SKANIME04</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ / ᴏᴡɴᴇʀ : <a href=https://t.me/SKANIME04>@SKANIME04</a></blockquote></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ <b>SK ANIME FILE STORE</b> ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @CARTOONFUNNY04</b>")
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT  = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "😂 Bhai seedha baat mat kar, /start dabao!"

OWNER_TAG      = os.environ.get("OWNER_TAG", "SKANIME04")
UPI_ID         = os.environ.get("UPI_ID", "20213904@axl")
QR_PIC         = os.environ.get("QR_PIC", "https://i.ibb.co/35QF8QMJ/QR.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "t.me/SKANIME04")

PRICE1, PRICE2, PRICE3 = os.environ.get("PRICE1", "0 rs"), os.environ.get("PRICE2", "60 rs"), os.environ.get("PRICE3", "150 rs")
PRICE4, PRICE5 = os.environ.get("PRICE4", "280 rs"), os.environ.get("PRICE5", "550 rs")

LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
