aimport asyncio
from nexichat.userbot.userbot import Userbot

if __name__ == "__main__":
    userbot = Userbot()
    asyncio.get_event_loop().run_until_complete(userbot.start())
from nexichat.userbot.userbot import Userbot

if __name__ == "__main__":
    userbot = Userbot()
    userbot.run()
