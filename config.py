from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "23321839"))
API_HASH = getenv("API_HASH", "71573a1db6821a2bc9e94eda20ad0e9b")
BOT_TOKEN = getenv("BOT_TOKEN", "5504187196:AAHfHSISH8M7IzqboqyM7GVnYF7m_ZxjF4g")
BOT_NAME = getenv("BOT_NAME","SpotifyMusics")
BOT_USERNAME = getenv("BOT_USERNAME", "SpotifyMusicsbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@DEVIL_ITS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "all_quiz_new")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b30c4862fba6928072177.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/b30c4862fba6928072177.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQDB_Hwh2HXhWoGeE2qfWLv6rOeOcEWnNwdZof7__KBo2znYC71E-z_Td5EmOy45u3xxdS7Hu-K7dLHC0maToGdiCneZqasnRffPrT3TWd1VFX9B_fdfATmQ5q87zos4TwhRw6eyeHpbuZV801klOSbVRPSZc2zlvFPN3riCwQ52D-fCFAYQASqRgDfwMK8pjjKqn-MtnvJocoqLZFGzhkhccLn-uJv2p_SJueD31b8Y6KVTTrjf1S1HPApGls3fJBDFMAnMLpiXFM5bzSyfWwXkPlM2bUTXlS-8yEKeTrsf9220-iWVNi8mq-S_vD6-GIv8_Z5Ze4tAsOg87FJm7hPiAAAAAToE2dEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5268363729").split()))
