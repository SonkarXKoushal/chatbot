from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = 26341381
# -------------------------------------------------------------
API_HASH = "2762d6b85975700ffddae249e13911cf"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "8044536901:AAEdh9Pj3iCvEF_r5aKASuXoY9d4VSaQ-to")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", 8009369344))
SUPPORT_GRP = "RIYA_chat_SUPPORT"
UPDATE_CHNL = "RiyaUpdates"
OWNER_USERNAME = "ll_hunter_lll"
