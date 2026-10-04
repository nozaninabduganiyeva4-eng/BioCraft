import asyncio
import logging
import sys
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

# UTF-8 stdout sozlash
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import BOT_TOKEN, BOT_NAME
from database import init_db

# Handler routerlar
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


async def handle_health(request):
    """Railway va serverlar uchun health-check handler"""
    return web.Response(
        text=f"{BOT_NAME} Telegram Bot is running 24/7 successfully!",
        content_type="text/plain",
        status=200,
    )


async def start_health_server():
    """Railway port talab qilsa, uni qondirish uchun yengil HTTP server"""
    port = int(os.getenv("PORT", 8080))
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"Health-check HTTP server running on 0.0.0.0:{port}")


async def set_bot_commands(bot: Bot):
    """Telegram bot buyruqlarini sozlash"""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
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

    # Agar Railway yoki hosting PORT taqdim etsa, health serverni yoqamiz
    if os.getenv("PORT"):
        try:
            await start_health_server()
        except Exception as e:
            logger.warning(f"Health serverni ishga tushirishda ogohlantirish: {e}")

    logger.info(f"Starting {BOT_NAME} Telegram Bot...")
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Routerlarni ulash
    dp.include_router(start_router)
    dp.include_router(bio_router)
    dp.include_router(username_router)
    dp.include_router(caption_router)
    dp.include_router(hashtag_router)
    dp.include_router(status_router)
    dp.include_router(settings_router)
    dp.include_router(profile_router)

    await set_bot_commands(bot)

    # Eski webhook va kutilayotgan so'rovlarni tozalash
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
        logger.info("Dastur to'xtatildi.")
