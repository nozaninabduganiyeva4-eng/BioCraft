import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from handlers.states import GenerationStates
from keyboards.inline_keyboards import get_cancel_keyboard, get_generation_actions_keyboard
from keyboards.main_menu import get_main_menu_keyboard
from database import check_rate_limit, record_successful_request, get_user_style
from services.gemini_service import ai_generate_bio
from config import AVAILABLE_STYLES

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == "🌟 Instagram BIO")
async def start_bio_flow(message: Message, state: FSMContext):
    await state.set_state(GenerationStates.waiting_for_bio_input)
    style_key = get_user_style(message.from_user.id)
    style_name = AVAILABLE_STYLES.get(style_key, {}).get("name", "✨ Aesthetic")

    text = (
        "🌟 <b>Instagram BIO Yaratish</b>\n\n"
        f"🎨 <i>Hozirgi uslub: {style_name}</i>\n\n"
        "O'zingiz yoki sahifangiz haqida bir necha so'z bilan yozib yuboring:\n"
        "<i>(Masalan: Ismingiz, kasbingiz, sevimli mashg'ulotlaringiz, yashash joyingiz yoki asosiy maqsadingiz)</i>\n\n"
        "✍️ <b>Matningizni kiriting:</b>"
    )
    await message.answer(text=text, reply_markup=get_cancel_keyboard(), parse_mode="HTML")


@router.message(GenerationStates.waiting_for_bio_input)
async def process_bio_input(message: Message, state: FSMContext):
    user_input = message.text.strip()
    if len(user_input) < 2:
        await message.answer("Iltimos, o'zingiz haqingizda bir oz batafsilroq ma'lumot kiriting:")
        return

    user_id = message.from_user.id
    can_request, reason, remaining = check_rate_limit(user_id)
    if not can_request:
        await message.answer(reason)
        return

    style_key = get_user_style(user_id)
    style_name = AVAILABLE_STYLES.get(style_key, {}).get("name", "✨ Aesthetic")

    wait_msg = await message.answer(
        f"⚡ <b>BioCraft AI</b> siz uchun <b>{style_name}</b> uslubida BIO variantlarini tayyorlamoqda...\n"
        "Iltimos, bir necha soniya kuting... ⏳",
        parse_mode="HTML",
    )

    try:
        result_text, from_cache = await ai_generate_bio(user_input, style_key)
        record_successful_request(user_id)

        # Holatni saqlab qo'yamiz (Qayta yaratish uchun)
        await state.update_data(last_bio_input=user_input)

        cache_note = " <i>(⚡ Keshdan tezkor yuklandi)</i>" if from_cache else ""
        header = f"✨ <b>Siz uchun Instagram BIO variantlari:</b>{cache_note}\n\n"

        await wait_msg.delete()
        await message.answer(
            text=header + result_text,
            reply_markup=get_generation_actions_keyboard("bio"),
            parse_mode="HTML",
        )
    except Exception as e:
        logger.error(f"BIO generatsiyasida xatolik: {e}")
        await wait_msg.delete()
        await message.answer(
            "⚠️ So'rovni bajarishda kutilmagan xatolik yuz berdi. Iltimos, birozdan so'ng qayta urinib ko'ring.",
            reply_markup=get_main_menu_keyboard(style_key),
        )


@router.callback_query(F.data == "regen_bio")
async def regen_bio_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_input = data.get("last_bio_input")
    if not last_input:
        await callback.answer("Avvalgi matn topilmadi. Iltimos, qaytadan yozing.", show_alert=True)
        return

    user_id = callback.from_user.id
    can_request, reason, remaining = check_rate_limit(user_id)
    if not can_request:
        await callback.answer(reason, show_alert=True)
        return

    style_key = get_user_style(user_id)
    await callback.answer("Qayta yaratilmoqda...")

    try:
        result_text, _ = await ai_generate_bio(last_input + " (yangi variantlar)", style_key)
        record_successful_request(user_id)

        header = "🔄 <b>Yangi Instagram BIO variantlari:</b>\n\n"
        await callback.message.edit_text(
            text=header + result_text,
            reply_markup=get_generation_actions_keyboard("bio"),
            parse_mode="HTML",
        )
    except Exception as e:
        logger.error(f"Regen bio error: {e}")
        await callback.message.answer("⚠️ Qayta yaratishda xatolik yuz berdi.")
