import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "755565555"))
    API_HASH = os.environ.get("API_HASH", "hchfggfhgg5545545")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "123555555hdghfdhff")
    STRING_SESSION = os.environ.get("STRING_SESSION", "hhhg")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "HunerThon")
    CHANNEL = os.environ.get("CHANNEL", "HunerThon")
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "")

