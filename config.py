import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1996499923:AAGVCjT4msY1AOHb-qtalwMsrwu0dD65k7g")
    APP_ID = int(os.environ.get("APP_ID", "3335796"))
    API_HASH = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")
    USER_NAME = os.environ.get("USER_NAME", "ez_harki_me")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "763990585").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
