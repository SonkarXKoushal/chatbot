import asyncio
import signal
from pyrogram import idle
from nexichat.userbot.userbot import Userbot

userbot = Userbot()

async def main():
    await userbot.start()
    await idle()
    await userbot.stop()

if __name__ == "__main__":
    asyncio.run(main())
