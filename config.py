# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28555306"))
API_HASH = getenv("API_HASH", "f1527275dd7c7965f36cf4f364999ad6")
BOT_TOKEN = getenv("BOT_TOKEN", "8181465356:AAGsLALKRsDSicovn5hSzyZ-qihR_1MMesw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8198445194").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aamirzsx:tajmahal0@cluster0.rbt2mlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4599641174")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-4599641174"))
