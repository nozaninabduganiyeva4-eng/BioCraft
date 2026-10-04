from aiogram import Router, F
from aiogram.types import Message
from database import get_user_profile
from config import DAILY_REQUEST_LIMIT, AVAILABLE_STYLES

router = Router()


@router.message(F.text == "👤 Profil & Limitlar")
async def show_profile(message: Message):
    user_id = message.from_user.id
    prof = get_user_profile(user_id)

    style_key = prof.get("selected_style", "aesthetic")
    style_label = AVAILABLE_STYLES.get(style_key, {}).get("name", "✨ Aesthetic")
    requests_today = prof.get("requests_today", 0)
    remaining_today = max(0, DAILY_REQUEST_LIMIT - requests_today)
    total_requests = prof.get("total_requests", 0)
    created_at = str(prof.get("created_at", "Yaqinda"))[:10]

    text = (
        "👤 <b>Foydalanuvchi Profili va Limitlar</b>\n\n"
        f"🆔 <b>ID:</b> <code>{user_id}</code>\n"
        f"🏷 <b>Ism:</b> {prof.get('first_name', 'Foydalanuvchi')}\n"
        f"🎨 <b>Tanlangan uslub:</b> {style_label}\n\n"
        "📊 <b>So'rovlar statistikasi:</b>\n"
        f"• 📅 Bugun ishlatildi: <b>{requests_today} / {DAILY_REQUEST_LIMIT}</b> ta\n"
        f"• ⚡ Qolgan limit: <b>{remaining_today}</b> ta\n"
        f"• 🚀 Jami yaratilgan kontentlar: <b>{total_requests}</b> ta\n"
        f"• 🗓 Ro'yxatdan o'tgan: {created_at}\n\n"
        "💡 <i>Eslatma: Kunlik bepul limit har kuni soat 00:00 da avtomatik yangilanadi.</i>"
    )
    await message.answer(text=text, parse_mode="HTML")
