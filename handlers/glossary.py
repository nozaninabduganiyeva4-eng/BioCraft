from aiogram import Router, F
from aiogram.types import Message
from data.glossary import GLOSSARY, search_term

router = Router()


@router.message(F.text == "📖 Terminlar Lug'ati")
async def glossary_menu(message: Message):
    sample_terms = list(GLOSSARY.keys())[:10]
    terms_list = ", ".join([f"<code>{t.capitalize()}</code>" for t in sample_terms])

    text = (
        "📖 <b>Biologik Terminlar Lug'ati</b>\n\n"
        "O'zingiz bilmoqchi bo'lgan biologik atama yoki terminni botga yozib yuboring (masalan: <i>Mitoz</i>, <i>Fotosintez</i>, <i>ATF</i>, <i>Genotip</i>).\n\n"
        f"<b>Mavjud ba'zi terminlar:</b>\n{terms_list} va boshqalar...\n\n"
        "🔍 Qidirish uchun so'zni shunchaki xabar sifatida yozing!"
    )
    await message.answer(text=text, parse_mode="HTML")


@router.message(F.text & ~F.text.startswith("/") & ~F.text.in_([
    "🧬 Bo'limlar",
    "🧪 Viktorina (Quiz)",
    "📖 Terminlar Lug'ati",
    "💡 Qiziqarli Fakt",
    "🏆 Reyting",
    "👤 Profilim",
    "ℹ️ Bot haqida",
]))
async def handle_term_search(message: Message):
    query = message.text.strip()
    if len(query) < 2:
        return

    matches = search_term(query)

    if matches:
        response_parts = [f"🔍 <b>'{query}' bo'yicha topilgan natijalar:</b>\n"]
        for term, definition in matches.items():
            response_parts.append(f"📌 <b>{term.capitalize()}</b>:\n{definition}\n")
        await message.answer(text="\n".join(response_parts), parse_mode="HTML")
    else:
        await message.answer(
            f"Afsuski, <b>'{query}'</b> bo'yicha ma'lumot topilmadi.\n"
            "Iltimos, so'z to'g'ri yozilganini tekshiring yoki boshqa terminni qidiring.",
            parse_mode="HTML",
        )
