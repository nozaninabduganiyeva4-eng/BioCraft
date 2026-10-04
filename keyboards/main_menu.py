from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="🧬 Bo'limlar"),
            KeyboardButton(text="🧪 Viktorina (Quiz)"),
        ],
        [
            KeyboardButton(text="📖 Terminlar Lug'ati"),
            KeyboardButton(text="💡 Qiziqarli Fakt"),
        ],
        [
            KeyboardButton(text="🏆 Reyting"),
            KeyboardButton(text="👤 Profilim"),
        ],
        [
            KeyboardButton(text="ℹ️ Bot haqida"),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Kerakli bo'limni tanlang...",
    )
