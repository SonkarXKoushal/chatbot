import logging
from pyrogram import Client
from pyrogram.enums import ParseMode
import config

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

app = Client(
    "nexichat_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    parse_mode=ParseMode.DEFAULT,
    plugins=dict(root="nexichat.idchatbot"),
)

def run():
    LOGGER.info("Starting Telegram Bot...")
    app.run()
