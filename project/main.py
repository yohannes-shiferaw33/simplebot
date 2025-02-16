import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from config import BOT_TOKEN, ADMIN_ID, CONNECT_DB, DB_URL
from utils.create_db import create_db
from aiogram.enums import ParseMode
from handlers.form import router
import asyncio
import sys
import psycopg_pool
from middleware.db_middleware import DBsession

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def create_pool():
    return psycopg_pool.AsyncConnectionPool(DB_URL)


async def start():
    await create_db()
    pooling=await create_pool()
    pooling.connection_class.autocommit=True
    dp.update.middleware(DBsession(pooling))
    dp.include_router(router=router)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(policy=asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start())
