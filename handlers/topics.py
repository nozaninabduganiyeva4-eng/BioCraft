from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from data.biology_topics import TOPICS
from keyboards.inline_keyboards import (
    get_topics_keyboard,
    get_sections_keyboard,
    get_section_detail_keyboard,
)

router = Router()


@router.message(F.text == "🧬 Bo'limlar")
async def show_topics(message: Message):
    text = (
        "🧬 <b>Biologiya Fan Bo'limlari</b>\n\n"
        "O'zingizni qiziqtirgan yo'nalishni tanlang va mavzular bilan batafsil tanishing:"
    )
    await message.answer(
        text=text,
        reply_markup=get_topics_keyboard(),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "back_topics")
async def back_to_topics(callback: CallbackQuery):
    text = (
        "🧬 <b>Biologiya Fan Bo'limlari</b>\n\n"
        "O'zingizni qiziqtirgan yo'nalishni tanlang va mavzular bilan batafsil tanishing:"
    )
    await callback.message.edit_text(
        text=text,
        reply_markup=get_topics_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data.startswith("topic_"))
async def show_topic_sections(callback: CallbackQuery):
    topic_key = callback.data.split("_")[1]
    topic = TOPICS.get(topic_key)

    if not topic:
        await callback.answer("Bo'lim topilmadi!", show_alert=True)
        return

    text = (
        f"{topic['title']}\n\n"
        f"<i>{topic['description']}</i>\n\n"
        "Quyidagi mavzulardan birini tanlang:"
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=get_sections_keyboard(topic_key),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data.startswith("sec_"))
async def show_section_content(callback: CallbackQuery):
    sec_id = callback.data.replace("sec_", "")

    # Qaysi bo'limga tegishli ekanligini topish
    found_sec = None
    found_topic_key = None

    for topic_key, topic in TOPICS.items():
        for sec in topic["sections"]:
            if sec["id"] == sec_id:
                found_sec = sec
                found_topic_key = topic_key
                break
        if found_sec:
            break

    if not found_sec:
        await callback.answer("Mavzu ma'lumoti topilmadi!", show_alert=True)
        return

    await callback.message.edit_text(
        text=found_sec["content"],
        reply_markup=get_section_detail_keyboard(found_topic_key),
        parse_mode="HTML",
    )
    await callback.answer()
