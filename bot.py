import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, BOT_NAME
from database import init_db

# Handler routerlarni import qilish
from handlers.start import router as start_router
from handlers.bio import router as bio_router
from handlers.username import router as username_router
from handlers.caption import router as caption_router
from handlers.hashtag import router as hashtag_router
from handlers.status import router as status_router
from handlers.settings import router as settings_router
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


async def set_bot_commands(bot: Bot):
    """Telegram botning asosiy buyruqlar menyusini sozlash"""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish (Bosh sahifa)"),
        BotCommand(command="bio", description="Instagram BIO yaratish"),
        BotCommand(command="username", description="Noyob username takliflari"),
        BotCommand(command="caption", description="Post & Story caption yozish"),
        BotCommand(command="hashtag", description="Mos hashtaglar to'plami"),
        BotCommand(command="status", description="Aesthetic status va iqtiboslar"),
        BotCommand(command="help", description="Qo'llanma va ma'lumot"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logger.info("Initializing BioCraft AI database...")
    init_db()

    logger.info(f"Starting {BOT_NAME} Telegram Bot...")
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Routerlarni tartib bilan ulash
    dp.include_router(start_router)
    dp.include_router(bio_router)
    dp.include_router(username_router)
    dp.include_router(caption_router)
    dp.include_router(hashtag_router)
    dp.include_router(status_router)
    dp.include_router(settings_router)
    dp.include_router(profile_router)

    await set_bot_commands(bot)

    # Kutilayotgan eski yangilanishlarni tozalash
    await bot.delete_webhook(drop_pending_updates=True)

    bot_info = await bot.get_me()
    logger.info(f"🚀 {BOT_NAME} muvaffaqiyatli ishga tushdi: @{bot_info.username} ({bot_info.first_name})")

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
