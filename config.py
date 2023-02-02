from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8391586"))
API_HASH = getenv("API_HASH", "b1a43ce85cad3c904b795c44c2aac9ef")
BOT_TOKEN = getenv("BOT_TOKEN", "5529036972:AAGSACijTZg7ym0fZlDdAWYdzv7Y-GraCEc")
BOT_NAME = getenv("BOT_NAME","musicbot")
BOT_USERNAME = getenv("BOT_USERNAME", "music_12223bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "U_8_U_2")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kingdom12a")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/3ea222257120c969e2afe.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/3ea222257120c969e2afe.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BAB1zJ0AXy899yaIU0V33j_zgif3j4qAqq6DWK2jCkjt05zFAXedOcwKcoJ7gC1F2mPGcFwzDdk4w-A7eG_zsMYfZuWuaovEstK1L8u2yqF8i-gBv9qcZpl9ydeagYp1ELpUwtxU_dT__tqRZZKu_90QfkN3vJ1yXZnxfR1tAT7YP2Z8K0ermCb7moLe-d9y1D7Pkgxc6ucbGElgSpn-i8OmE2tfWZ0RhCnBFIzkprIPcCgn2F5d1TAeuJGZUpkLU71Kxm4WRFJ89j0QGsQIKk5ZpR7tEkxfPK7nW_C_Izdscq6lHIntpn_ZApbQUiYK23DphHw54itnPsOZ5CtBPhgTE1ovzQAAAAB5eY1uAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "901751747").split()))
