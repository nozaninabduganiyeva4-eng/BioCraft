import os
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext

from config import BANNER_PATH, BOT_NAME, AVAILABLE_STYLES
from database import register_or_update_user, get_user_style, set_user_style
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.inline_keyboards import get_style_selector_keyboard

router = Router()


WELCOME_CAPTION = (
    f"👋 Assalomu alaykum! <b>{BOT_NAME}</b> — Instagram Bio & SMM sun'iy intellekt yordamchisiga xush kelibsiz!\n\n"
    "Bu bot orqali ijtimoiy tarmoq profillaringizni bir necha soniyada professional va betakror darajaga olib chiqishingiz mumkin:\n\n"
    "• 🌟 <b>Instagram BIO:</b> O'zingiz yoki brendingiz haqida ma'lumot bering — AI chiroyli emojilar va format bilan tayyorlab beradi;\n"
    "• 🏷 <b>Noyob Username:</b> Profilingiz uchun jozibali, esda qolarli nikneymlar;\n"
    "• ✍️ <b>Post & Story Caption:</b> Kuchli Hook, qiziqarli matn va harakatga chaqiruvchi postlar;\n"
    "• #️⃣ <b>Mos Hashtaglar:</b> Organik o'sish uchun saralangan hashtaglar to'plami;\n"
    "• 💬 <b>Status & Iqtiboslar:</b> Aesthetic, falsafiy va motivatsion sitatalar;\n"
    "• 🎨 <b>5 xil uslub:</b> <i>Aesthetic, Minimal, Professional, Funny, Creative</i>.\n\n"
    "Quyidagi menyu orqali kerakli bo'limni tanlang va profilingizni yangilang! 👇"
)


@router.message(CommandStart())
async def handle_start(message: Message, state: FSMContext):
    await state.clear()
    user = message.from_user
    register_or_update_user(
        user_id=user.id,
        first_name=user.first_name or "Foydalanuvchi",
        username=user.username,
    )
    style = get_user_style(user.id)
    menu_kb = get_main_menu_keyboard(style)

    if BANNER_PATH.exists():
        try:
            photo = FSInputFile(str(BANNER_PATH))
            await message.answer_photo(
                photo=photo,
                caption=WELCOME_CAPTION,
                reply_markup=menu_kb,
                parse_mode="HTML",
            )
            return
        except Exception:
            pass

    # Agar rasm yuklashda xatolik bo'lsa matn yuboriladi
    await message.answer(
        text=WELCOME_CAPTION,
        reply_markup=menu_kb,
        parse_mode="HTML",
    )


@router.message(Command("help"))
@router.message(F.text == "ℹ️ Bot haqida")
async def handle_help(message: Message):
    help_text = (
        f"ℹ️ <b>{BOT_NAME} — Qo'llanma</b>\n\n"
        "Bot Google Gemini ilg'or sun'iy intellekti asosida ishlaydi va ijtimoiy tarmoqlar uchun "
        "kontent yaratish jarayonini bir necha barobar tezlashtiradi.\n\n"
        "<b>📌 Asosiy buyruqlar:</b>\n"
        "• 🌟 <b>Instagram BIO</b> — Profilingiz bio qismi uchun 4 xil variant;\n"
        "• 🏷 <b>Noyob Username</b> — 10+ xil zamonaviy nikneym g'oyalari;\n"
        "• ✍️ <b>Caption</b> — Post va stories uchun to'liq matn;\n"
        "• #️⃣ <b>Hashtaglar</b> — Katta, o'rta va nisha hashtag to'plamlari;\n"
        "• 💬 <b>Status & Iqtiboslar</b> — Kunlik ilhomlantiruvchi statuslar;\n"
        "• 🎨 <b>Uslub tanlash</b> — O'zingizga yoqqan ohangni tanlang (Aesthetic, Minimal, Professional va h.k.).\n\n"
        "🔒 <i>Barcha ma'lumotlaringiz xavfsiz va maxfiy saqlanadi.</i>\n"
        "Savol va takliflar uchun: @takeabiobot"
    )
    await message.answer(text=help_text, parse_mode="HTML")


@router.callback_query(F.data == "go_main_menu")
async def callback_go_main_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    style = get_user_style(callback.from_user.id)
    await callback.message.answer(
        text="🏠 <b>Asosiy Menyu</b>\nKerakli bo'limni tanlang:",
        reply_markup=get_main_menu_keyboard(style),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data == "cancel_action")
async def callback_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    style = get_user_style(callback.from_user.id)
    await callback.message.edit_text("❌ Amaliyot bekor qilindi.")
    await callback.message.answer(
        text="Bosh menyuga qaytdingiz:",
        reply_markup=get_main_menu_keyboard(style),
    )
    await callback.answer()
