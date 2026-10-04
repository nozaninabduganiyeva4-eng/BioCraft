from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database import get_user_stats, get_top_users

router = Router()


@router.message(F.text == "👤 Profilim")
async def show_profile(message: Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)

    if not stats:
        await message.answer("Siz haqingizda ma'lumot topilmadi. Qaytadan /start bosing.")
        return

    accuracy = (
        round((stats["correct_answers"] / stats["quizzes_taken"]) * 100, 1)
        if stats["quizzes_taken"] > 0
        else 0
    )

    text = (
        "👤 <b>Sizning Profillaringiz</b>\n\n"
        f"🏷 <b>Ism:</b> {stats['first_name']}\n"
        f"🆔 <b>ID:</b> <code>{stats['user_id']}</code>\n"
        f"⭐ <b>Jami ball:</b> {stats['score']} ball\n"
        f"🧪 <b>Yechilgan testlar:</b> {stats['quizzes_taken']} ta\n"
        f"✅ <b>To'g'ri javoblar:</b> {stats['correct_answers']} ta\n"
        f"🎯 <b>Aniqlik darajasi:</b> {accuracy}%\n"
        f"📅 <b>Ro'yxatdan o'tgan:</b> {stats['joined_at'][:10]}\n\n"
        "<i>Viktorinada qatnashib ballaringizni oshiring va reytingda yetakchi bo'ling!</i>"
    )
    await message.answer(text=text, parse_mode="HTML")


@router.message(F.text == "🏆 Reyting")
@router.callback_query(F.data == "view_ranking")
async def show_ranking(event: Message | CallbackQuery):
    top_users = get_top_users(limit=10)

    lines = ["🏆 <b>BioCraft — Bilimdonlar Reytingi (Top-10)</b>\n"]
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if not top_users:
        lines.append("Hozircha reytingda hech kim yo'q. Birinchi bo'lib test ishlang!")
    else:
        for idx, u in enumerate(top_users):
            medal = medals[idx] if idx < len(medals) else f"{idx+1}."
            name = u["first_name"] or "Foydalanuvchi"
            lines.append(
                f"{medal} <b>{name}</b> — <b>{u['score']} ball</b> "
                f"<i>({u['correct_answers']}/{u['quizzes_taken']} to'g'ri)</i>"
            )

    ranking_text = "\n".join(lines)

    if isinstance(event, CallbackQuery):
        await event.message.answer(text=ranking_text, parse_mode="HTML")
        await event.answer()
    else:
        await event.answer(text=ranking_text, parse_mode="HTML")
