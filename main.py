import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import os
from dotenv import load_dotenv
load_dotenv()

bottoken = os.getenv('BOT_TOKEN')
bot = Bot(token=bottoken)
dp = Dispatcher()
@dp.message(CommandStart())
async def d(j: Message):
    await j.answer('Botimizga xush kelibsiz')
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())