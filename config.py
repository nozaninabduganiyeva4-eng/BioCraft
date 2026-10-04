import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("DIQQAT: .env faylida BOT_TOKEN topilmadi!")

if not GEMINI_API_KEY:
    raise ValueError("DIQQAT: .env faylida GEMINI_API_KEY topilmadi!")

# Fayl va papka yo'llari
DB_PATH = BASE_DIR / "biocraft.db"
ASSETS_DIR = BASE_DIR / "assets"
BANNER_PATH = ASSETS_DIR / "banner.png"

# Bot ma'lumotlari
BOT_NAME = "BioCraft AI"
BOT_USERNAME = "@takeabiobot"
VERSION = "2.0.0"

# Limitlar va Kesh sozlamalari
COOLDOWN_SECONDS = 5  # Foydalanuvchi so'rovlari orasidagi kutish vaqti
DAILY_REQUEST_LIMIT = 50  # Bir foydalanuvchi uchun kunlik bepul limit
CACHE_EXPIRY_HOURS = 24  # Takroriy so'rovlar keshi amal qilish muddati

# Uslublar ro'yxati
AVAILABLE_STYLES = {
    "aesthetic": {
        "name": "✨ Aesthetic",
        "desc": "Nafis, shinam, chiroyli shrift va simvollar uyg'unligida",
        "instruction": "Uslub: Aesthetic, sokin, didli, nafis emojilar va chiroyli tartib bilan.",
    },
    "minimal": {
        "name": "🌿 Minimal",
        "desc": "Sodda, qisqa, aniq va ortiqcha bezaklarsiz",
        "instruction": "Uslub: Minimalistik, juda qisqa, lo'nda, oz miqdorda aniq emojilar bilan.",
    },
    "professional": {
        "name": "💼 Professional",
        "desc": "Biznes, ekspert, ishonchli va rasmiy ohangda",
        "instruction": "Uslub: Professional, biznesga mos, ishonch uyg'otuvchi va ekspert darajasida.",
    },
    "funny": {
        "name": "😂 Funny",
        "desc": "Samimiy, hazilomuz, kulgili va erkin kayfiyatda",
        "instruction": "Uslub: Qiziqarli, hazilomuz, samimiy, do'stona va kulgili ohangda.",
    },
    "creative": {
        "name": "🚀 Creative",
        "desc": "Kreativ, noodatiy, diqqatni tortuvchi va ilhomlantiruvchi",
        "instruction": "Uslub: Juda kreativ, noodatiy, e'tiborni darhol tortadigan va ilhomlantiruvchi.",
    },
}
