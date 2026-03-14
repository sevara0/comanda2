import asyncio
from aiogram import  Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("hello world")

# kolya qosti
@dp.message(Command("admin"))
async def admin(message:Message):
    await message.answer("https://t.me/+QxVOy6y_wXpmYmIy")

@dp.message(Command("maglumat"))
async def maglumat(message:Message):
    await message.answer("hazirshe maglumat joq")

@dp.message(Command("kamentarya"))
async def kamentarya(message:Message):
    await message.answer("hazirshe maglumat joq")


async def main():
    print("bot istedi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())