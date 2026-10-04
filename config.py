import os
from pathlib import Path
from dotenv import load_dotenv

# .env faylini yuklash
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Asosiy sozlamalar
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("DIQQAT: .env faylida BOT_TOKEN topilmadi! Iltimos, .env faylini to'ldiring.")

DB_PATH = BASE_DIR / "biocraft.db"

# Bot ma'lumotlari
BOT_NAME = "BioCraft"
BOT_USERNAME = "@takeabiobot"
VERSION = "1.0.0"
ADMIN_ID = os.getenv("ADMIN_ID")
