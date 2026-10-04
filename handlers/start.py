from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.main_menu import get_main_menu_keyboard
from database import register_user
from config import BOT_NAME

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    user = message.from_user
    register_user(
        user_id=user.id,
        first_name=user.first_name or "Foydalanuvchi",
        username=user.username,
    )

    welcome_text = (
        f"👋 Assalomu alaykum, <b>{user.first_name}</b>!\n\n"
        f"🌿 <b>{BOT_NAME}</b> — biologiya fani bo'yicha interaktiv ta'lim va viktorina botiga xush kelibsiz!\n\n"
        "Bu yerda siz:\n"
        "• 🧬 Biologiya asosiy bo'limlari bo'yicha nazariy bilimlarni o'rganishingiz;\n"
        "• 🧪 Interaktiv testlar va viktorinalarda qatnashib ball to'plashingiz;\n"
        "• 📖 Muhim biologik terminlar lug'atidan qidirishingiz;\n"
        "• 💡 Hayratlanarli tirik tabiat faktlari bilan tanishishingiz;\n"
        "• 🏆 Boshqa foydalanuvchilar bilan reytingda bellashishingiz mumkin!\n\n"
        "Quyidagi menyu tugmalaridan birini tanlang va sayohatingizni boshlang! 👇"
    )

    await message.answer(
        text=welcome_text,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="HTML",
    )


@router.message(Command("help"))
@router.message(F.text == "ℹ️ Bot haqida")
async def handle_help(message: Message):
    help_text = (
        f"ℹ️ <b>{BOT_NAME} Boti Haqida</b>\n\n"
        "Bot abituriyentlar, maktab o'quvchilari va biologiyaga qiziquvchilar uchun "
        "interaktiv ta'lim platformasi sifatida yaratilgan.\n\n"
        "<b>📌 Asosiy bo'limlar:</b>\n"
        "• 🧬 <b>Bo'limlar:</b> Botanika, Zoologiya, Odam anatomiyasi, Sitologiya, Genetika va Ekologiya.\n"
        "• 🧪 <b>Viktorina:</b> Har bir to'g'ri javob uchun +10 ball beriladi.\n"
        "• 📖 <b>Terminlar Lug'ati:</b> Istalgan biologik atamani matn qilib yozsangiz, bot uning ma'nosini topib beradi.\n"
        "• 💡 <b>Qiziqarli Fakt:</b> Tirik tabiat mo'jizalari haqida qiziqarli ma'lumotlar.\n"
        "• 🏆 <b>Reyting:</b> Eng faol va eng ko'p ball to'plagan bilimdonlar ro'yxati.\n\n"
        "Savol va takliflar uchun: @takeabiobot"
    )
    await message.answer(text=help_text, parse_mode="HTML")
