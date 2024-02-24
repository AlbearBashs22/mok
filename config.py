from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://a.top4top.io/p_2929boy350.jpg")
START_IMG = getenv("START_IMG", "https://a.top4top.io/p_2929boy350.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sh0wming_2")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CC_MM_00")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6236388211").split()))


FAILED = "https://a.top4top.io/p_2929boy350.jpg"
