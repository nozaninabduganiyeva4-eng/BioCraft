import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand

from config import BOT_TOKEN, BOT_NAME
from database import init_db

# Handler routerlarni import qilish
from handlers.start import router as start_router
from handlers.topics import router as topics_router
from handlers.quiz import router as quiz_router
from handlers.glossary import router as glossary_router
from handlers.facts import router as facts_router
from handlers.profile import router as profile_router

# Logging sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


async def set_main_menu(bot: Bot):
    """Telegram bot buyruqlar menyusini o'rnatish"""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam va qo'llanma"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logger.info("Initializing BioCraft database...")
    init_db()

    logger.info(f"Starting {BOT_NAME} Telegram Bot...")
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Routerlarni ulash
    dp.include_router(start_router)
    dp.include_router(topics_router)
    dp.include_router(quiz_router)
    dp.include_router(facts_router)
    dp.include_router(profile_router)
    dp.include_router(glossary_router)

    await set_main_menu(bot)

    # Eski kutilayotgan yangilanishlarni (updates) tozalash
    await bot.delete_webhook(drop_pending_updates=True)

    bot_info = await bot.get_me()
    logger.info(f"Bot muvaffaqiyatli ishga tushdi: @{bot_info.username} ({bot_info.first_name})")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot to'xtatildi.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Dastur foydalanuvchi tomonidan to'xtatildi.")
