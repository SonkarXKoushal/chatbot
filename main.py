import signal
import sys
from pyrogram import idle
from nexichat.userbot.userbot import Userbot

userbot = None

def shutdown_handler(signum, frame):
    print("Shutdown signal received, stopping bot...")
    try:
        if userbot:
            userbot.stop()
    finally:
        sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

if __name__ == "__main__":
    userbot = Userbot()
    idle()
