import signal
import sys
import asyncio
from pyrogram import idle
from nexichat.userbot.userbot import Userbot

userbot = None
loop = asyncio.get_event_loop()

def shutdown_handler(signum, frame):
    print("Shutdown signal received, stopping bot...")
    async def _shutdown():
        if userbot:
            await userbot.stop()
    loop.run_until_complete(_shutdown())
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

if __name__ == "__main__":
    userbot = Userbot()
    idle()
