from typing import Callable, Any, Dict, Awaitable
from aiogram.types import TelegramObject
from aiogram import BaseMiddleware
from psycopg_pool import AsyncConnectionPool
from utils.db_request import Request

class DBsession(BaseMiddleware):
    def __init__(self, connector: AsyncConnectionPool):
        super().__init__()
        self.connector=connector
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any])->Any:
        async with self.connector.connection() as connect:
            data['request'] = Request(connect)
            return await handler(event, data)