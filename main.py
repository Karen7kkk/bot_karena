import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.handlers import start, help, echo


async def main():
    # Включаем логирование, чтобы видеть ошибки
    logging.basicConfig(level=logging.INFO)

    # Создаем объекты бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры (обработчики)
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)  # этот обработчик должен быть последним!

    # Запускаем поллинг
    await dp.start_polling(bot)


if name == "__main__":
    asyncio.run(main())
