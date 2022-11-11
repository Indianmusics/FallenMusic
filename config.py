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
SESSION_NAME = getenv("SESSION_NAME", "BQARNeB5ya-orOrrgNB4pC3nCaFH9AAyit2f8i9XizN_dh8Y7t1u-oL5m2bjPXNEJlDdO1LBaJtSa1_HGHlN4kbHzABzpxzYjQYTkKV7zjy9H6dZnjxEHzo4tFv_a_XHKB5QpqBItG0BSATs69bZcp9dnkHdbL8bRShRJ2HkjQwDZJFYq2gP4NmeTBH1krMnOPh5OFLw8IcXsYNJW4luelWXaf9QIyxhyQCIWr2ChHjBzb3ipgVig6mOveziO6CZHajRMdNRBLnGLprpX8YOrLJ-rkQevqap2enNwFUTXl-Z4ve1G2WLwwGqNwdplS5ikiHVlvpjSHiwQiIAZrvcQS46AAAAAToE2dEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5268363729").split()))
