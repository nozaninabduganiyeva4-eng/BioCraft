from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import AVAILABLE_STYLES


def get_main_menu_keyboard(current_style_key: str = "aesthetic") -> ReplyKeyboardMarkup:
    style_label = AVAILABLE_STYLES.get(current_style_key, {}).get("name", "✨ Aesthetic")

    keyboard = [
        [
            KeyboardButton(text="🌟 Instagram BIO"),
            KeyboardButton(text="🏷 Noyob Username"),
        ],
        [
            KeyboardButton(text="✍️ Post & Story Caption"),
            KeyboardButton(text="#️⃣ Mos Hashtaglar"),
        ],
        [
            KeyboardButton(text="💬 Status & Iqtiboslar"),
            KeyboardButton(text=f"🎨 Uslub: {style_label}"),
        ],
        [
            KeyboardButton(text="👤 Profil & Limitlar"),
            KeyboardButton(text="ℹ️ Bot haqida"),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Funksiyani tanlang yoki matn yuboring...",
    )
