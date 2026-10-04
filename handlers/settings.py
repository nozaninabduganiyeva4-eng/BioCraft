from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from config import AVAILABLE_STYLES
from database import get_user_style, set_user_style
from keyboards.inline_keyboards import get_style_selector_keyboard
from keyboards.main_menu import get_main_menu_keyboard

router = Router()


def get_styles_description_text(current_style: str) -> str:
    lines = [
        "🎨 <b>BioCraft AI — Uslubni Tanlash</b>\n",
        "O'zingizga ma'qul ohang va formatni tanlang. AI barcha matnlarni shu uslubga moslab tayyorlaydi:\n",
    ]
    for key, data in AVAILABLE_STYLES.items():
        active_mark = " 👉 <b>[Faol]</b>" if key == current_style else ""
        lines.append(f"• <b>{data['name']}</b>{active_mark}\n  <i>{data['desc']}</i>")

    lines.append("\nQuyidagi tugmalardan birini bosing:")
    return "\n".join(lines)


@router.message(F.text.startswith("🎨 Uslub"))
async def message_change_style(message: Message):
    current = get_user_style(message.from_user.id)
    text = get_styles_description_text(current)
    await message.answer(
        text=text,
        reply_markup=get_style_selector_keyboard(current),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "change_style")
async def callback_change_style(callback: CallbackQuery):
    current = get_user_style(callback.from_user.id)
    text = get_styles_description_text(current)
    await callback.message.answer(
        text=text,
        reply_markup=get_style_selector_keyboard(current),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data.startswith("set_style_"))
async def callback_set_style(callback: CallbackQuery):
    new_style = callback.data.replace("set_style_", "")
    if new_style not in AVAILABLE_STYLES:
        await callback.answer("Noto'g'ri uslub!", show_alert=True)
        return

    set_user_style(callback.from_user.id, new_style)
    style_info = AVAILABLE_STYLES[new_style]

    await callback.answer(f"Uslub o'zgartirildi: {style_info['name']}")

    text = (
        f"✅ <b>Uslub muvaffaqiyatli saqlandi!</b>\n\n"
        f"Tanlangan uslub: <b>{style_info['name']}</b>\n"
        f"<i>{style_info['desc']}</i>\n\n"
        "Endi yaratiladigan barcha BIO, username, caption va statuslar shu uslubda bo'ladi."
    )

    await callback.message.edit_text(text=text, parse_mode="HTML")
    await callback.message.answer(
        text="Quyidagi bo'limlardan foydalanishingiz mumkin:",
        reply_markup=get_main_menu_keyboard(new_style),
    )
