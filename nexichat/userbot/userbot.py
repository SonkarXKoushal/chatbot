from pyrogram import Client
import config
import asyncio
import logging

LOGGER = logging.getLogger(__name__)


class Userbot:
    def __init__(self):
        self.app = Client(
            name="VIPAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="nexichat.idchatbot"),
        )

    async def start(self):
        LOGGER.info("Starting Id chatbot...")

        await self.app.start()

        try:
            await self.app.join_chat("RIYA_network")
            await self.app.join_chat("riya_CHAT_support")
            await self.app.join_chat("SIGMA_BOT_NETWORK")
            await self.app.join_chat("BIT_networks")
        except Exception:
            pass

        LOGGER.info(f"Id-Chatbot Started as {self.app.me.first_name}")

    async def stop(self):
        LOGGER.info("Stopping Id-Chatbot...")
        await self.app.stop()
