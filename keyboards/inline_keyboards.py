from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AVAILABLE_STYLES


def get_style_selector_keyboard(current_style: str) -> InlineKeyboardMarkup:
    buttons = []
    for key, data in AVAILABLE_STYLES.items():
        is_active = "✅ " if key == current_style else ""
        text = f"{is_active}{data['name']}"
        buttons.append([InlineKeyboardButton(text=text, callback_data=f"set_style_{key}")])
    buttons.append([InlineKeyboardButton(text="🏠 Asosiy menyuga qaytish", callback_data="go_main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_generation_actions_keyboard(task_type: str) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="🔄 Qayta yaratish", callback_data=f"regen_{task_type}"),
            InlineKeyboardButton(text="🎨 Uslubni o'zgartirish", callback_data="change_style"),
        ],
        [
            InlineKeyboardButton(text="🏠 Asosiy Menyu", callback_data="go_main_menu"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel_action")]
        ]
    )
