from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from data.facts import get_random_fact
from keyboards.inline_keyboards import get_fact_keyboard

router = Router()


@router.message(F.text == "💡 Qiziqarli Fakt")
async def show_fact(message: Message):
    fact = get_random_fact()
    text = (
        "💡 <b>Tirik Tabiatning Hayratlanarli Fakti</b>\n\n"
        f"{fact}"
    )
    await message.answer(
        text=text,
        reply_markup=get_fact_keyboard(),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "next_fact")
async def next_fact_callback(callback: CallbackQuery):
    fact = get_random_fact()
    text = (
        "💡 <b>Tirik Tabiatning Hayratlanarli Fakti</b>\n\n"
        f"{fact}"
    )
    await callback.message.edit_text(
        text=text,
        reply_markup=get_fact_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()
