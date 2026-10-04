import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from data.quiz_questions import QUIZ_QUESTIONS
from keyboards.inline_keyboards import get_quiz_keyboard, get_next_quiz_keyboard
from database import record_quiz_answer

router = Router()


def get_random_question():
    return random.choice(QUIZ_QUESTIONS)


def get_question_by_id(qid: int):
    for q in QUIZ_QUESTIONS:
        if q["id"] == qid:
            return q
    return None


@router.message(F.text == "🧪 Viktorina (Quiz)")
async def start_quiz_command(message: Message):
    q = get_random_question()
    text = (
        f"🧪 <b>Biologiya Viktorinasi | {q['category']}</b>\n\n"
        f"❓ <b>Savol:</b>\n{q['question']}\n\n"
        "To'g'ri javobni tanlang:"
    )
    await message.answer(
        text=text,
        reply_markup=get_quiz_keyboard(q["id"], q["options"]),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "start_quiz")
@router.callback_query(F.data == "next_quiz")
async def next_quiz_callback(callback: CallbackQuery):
    q = get_random_question()
    text = (
        f"🧪 <b>Biologiya Viktorinasi | {q['category']}</b>\n\n"
        f"❓ <b>Savol:</b>\n{q['question']}\n\n"
        "To'g'ri javobni tanlang:"
    )
    await callback.message.edit_text(
        text=text,
        reply_markup=get_quiz_keyboard(q["id"], q["options"]),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data.startswith("ans_"))
async def handle_answer(callback: CallbackQuery):
    parts = callback.data.split("_")
    question_id = int(parts[1])
    selected_idx = int(parts[2])

    q = get_question_by_id(question_id)
    if not q:
        await callback.answer("Savol ma'lumoti topilmadi!", show_alert=True)
        return

    is_correct = selected_idx == q["correct_index"]
    points = q["points"] if is_correct else 0

    record_quiz_answer(
        user_id=callback.from_user.id,
        question_id=question_id,
        is_correct=is_correct,
        points=points,
    )

    status_icon = "✅ <b>To'g'ri javob!</b>" if is_correct else "❌ <b>Noto'g'ri javob!</b>"
    correct_option = q["options"][q["correct_index"]]

    result_text = (
        f"{status_icon}\n\n"
        f"❓ <b>Savol:</b> {q['question']}\n\n"
        f"🎯 <b>To'g'ri javob:</b> {correct_option}\n"
        f"💡 <b>Izoh:</b> {q['explanation']}\n\n"
        f"{'🎉 Sizga +' + str(q['points']) + ' ball berildi!' if is_correct else 'Keyingi savolda omad tilaymiz!'}"
    )

    await callback.message.edit_text(
        text=result_text,
        reply_markup=get_next_quiz_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer("Javobingiz qabul qilindi!")
