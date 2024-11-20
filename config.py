import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID",13404637))
API_HASH = getenv("API_HASH","a069bf02806468fe18427ab6b9a3bb6c")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7751992632:AAHPHGL7y-RjCWzvCBTOg2K6pXFtreH5KmI")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_hunter_lll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","riyamusicrobot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002356335631))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7668520999))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ksdofficial8/BADNAMXMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ksd_bot_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/team_riya_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BQD7IGgADPG6zBKdTx2owhrJMDWEAZGNT_S5Wa8OXpvKi7GMuqbcFwLVI4kxMvez-opRd2Mjoisd6S4XI4UExATSbxE98aUJVgGx4UGQTOCPnhc_zpQdhjrNx9sqpI1uYaLySgD5gYRshBj-R4SxfsWWo3XYOHMHObTz--GsJBHdELPZ8TBQGZ1rc2t7Etk36gNYbPJwTZvZMBfTKwxF2DsbbreLlSvhefTyIi5kLm0CuzE0U0yJpPCNyeaaNaLqtyASb4Ki3eLpSuayqjadxj1Jrh8HCwrF5-_C0mGmLK9rOSbOerrG9M_eCp3Dx9qDj2q17bcyXa_rWSqYPxe-E3HSFH-k1wAAAAGS2YzdAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/wzwggt.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/wzwggt.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
STATS_IMG_URL = "https://files.catbox.moe/bcg7x4.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/wzwggt.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/wzwggt.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/wzwggt.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
