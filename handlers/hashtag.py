import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from handlers.states import GenerationStates
from keyboards.inline_keyboards import get_cancel_keyboard, get_generation_actions_keyboard
from keyboards.main_menu import get_main_menu_keyboard
from database import check_rate_limit, record_successful_request, get_user_style
from services.gemini_service import ai_generate_hashtags
from config import AVAILABLE_STYLES

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == "#️⃣ Mos Hashtaglar")
async def start_hashtag_flow(message: Message, state: FSMContext):
    await state.set_state(GenerationStates.waiting_for_hashtag_input)
    style_key = get_user_style(message.from_user.id)
    style_name = AVAILABLE_STYLES.get(style_key, {}).get("name", "✨ Aesthetic")

    text = (
        "#️⃣ <b>Instagram Hashtag Generator</b>\n\n"
        f"🎨 <i>Hozirgi uslub: {style_name}</i>\n\n"
        "Post yoki video yo'nalishini yozing:\n"
        "<i>(Masalan: Moda va kiyimlar, Sayohat Samarqand, IT dasturlash, Go'zallik saloni, Shaxsiy rivojlanish)</i>\n\n"
        "🔍 <b>Mavzuni kiriting:</b>"
    )
    await message.answer(text=text, reply_markup=get_cancel_keyboard(), parse_mode="HTML")


@router.message(GenerationStates.waiting_for_hashtag_input)
async def process_hashtag_input(message: Message, state: FSMContext):
    user_input = message.text.strip()
    if len(user_input) < 2:
        await message.answer("Iltimos, mavzuni aniqroq kiriting:")
        return

    user_id = message.from_user.id
    can_request, reason, remaining = check_rate_limit(user_id)
    if not can_request:
        await message.answer(reason)
        return

    style_key = get_user_style(user_id)
    wait_msg = await message.answer(
        "⚡ <b>BioCraft AI</b> eng mos va samarali hashtaglar to'plamini tuzmoqda... ⏳",
        parse_mode="HTML",
    )

    try:
        result_text, from_cache = await ai_generate_hashtags(user_input, style_key)
        record_successful_request(user_id)
        await state.update_data(last_hashtag_input=user_input)

        cache_note = " <i>(⚡ Keshdan)</i>" if from_cache else ""
        header = f"#️⃣ <b>Siz uchun saralangan hashtaglar:</b>{cache_note}\n\n"

        await wait_msg.delete()
        await message.answer(
            text=header + result_text,
            reply_markup=get_generation_actions_keyboard("hashtag"),
            parse_mode="HTML",
        )
    except Exception as e:
        logger.error(f"Hashtag generatsiyasida xatolik: {e}")
        await wait_msg.delete()
        await message.answer(
            "⚠️ So'rovni bajarishda xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.",
            reply_markup=get_main_menu_keyboard(style_key),
        )


@router.callback_query(F.data == "regen_hashtag")
async def regen_hashtag_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_input = data.get("last_hashtag_input")
    if not last_input:
        await callback.answer("Avvalgi mavzu topilmadi. Qaytadan kiriting.", show_alert=True)
        return

    user_id = callback.from_user.id
    can_request, reason, remaining = check_rate_limit(user_id)
    if not can_request:
        await callback.answer(reason, show_alert=True)
        return

    style_key = get_user_style(user_id)
    await callback.answer("Yangi hashtaglar to'plami tayyorlanmoqda...")

    try:
        result_text, _ = await ai_generate_hashtags(last_input + " (alternativ)", style_key)
        record_successful_request(user_id)

        header = "🔄 <b>Yangi hashtaglar to'plami:</b>\n\n"
        await callback.message.edit_text(
            text=header + result_text,
            reply_markup=get_generation_actions_keyboard("hashtag"),
            parse_mode="HTML",
        )
    except Exception as e:
        logger.error(f"Regen hashtag error: {e}")
        await callback.message.answer("⚠️ Qayta yaratishda xatolik yuz berdi.")
