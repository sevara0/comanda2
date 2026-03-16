import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")


bas_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='baylanis'),KeyboardButton(text='Kanallar')],
        [KeyboardButton(text='sozlama')]
    ],
    resize_keyboard=True
)

baylanis_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='telefon nomer'),KeyboardButton(text='chatqa baylanisiw')],
        [KeyboardButton(text='Bas menyuga qaytiw')]
    ],
    resize_keyboard=True
)

#Chatqa baylanisiw
chat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Admin',url='https://t.me/ywywccwusvcyw_my_bot'),]
    ]

)
#Kanallar_menyu
Kanallar_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='telegram',url='https://t.me/xojanawil_rabota'),],
        [InlineKeyboardButton(text='Instagram',url='https://www.instagram.com/a.knmjva/'),],
        [InlineKeyboardButton(text='Youtube',url='https://youtube.com/@intelproduction?si=JlLCP7AZ_nNf0A-Q'),],
        [InlineKeyboardButton(text='Tasdiqlaw',callback_data='tasdiqlaw')]
    ]
)

bottoken = '8364915952:AAFjyxDwbfxB_YesB_wfeviFbHPhRR9pbgs'
bot = Bot(token=bottoken)
dp = Dispatcher()

@dp.message(CommandStart())
async def d(j: Message):
    await j.answer('Botimizga xush kelibsiz', reply_markup=bas_menu)

@dp.message(Command('jardem'))
async def d(j: Message):
    await j.answer('Qanday jardem kerek')

# menularg'a atvet
@dp.message()
async def baylanis(j: Message):
    txt = j.text
    if txt == 'baylanis':
        await j.answer('Adminge baylanisiw ushin tomendegi menyulardan paydalanin',reply_markup=baylanis_menyu)
    elif txt == 'Kanallar':
        await j.answer('Bizdin kanallar',reply_markup=Kanallar_menyu)

    #baylanis menyu
    elif txt == 'telefon nomer':
        await j.answer('+998 91-255-53-09')
    elif txt == 'chatqa baylanisiw':
        await j.answer('Admin chati',reply_markup=chat_menu)

    elif txt == 'Bas menyuga qaytiw':
        await j.answer('Siz bas menyuga qayttiniz',  reply_markup=baylanis_menyu)

@dp.callback_query()
async def tasdiqlaw(call: CallbackQuery):
    if call.data == 'tasdiqlaw':
        await call.message.answer(
            f"{call.from_user.first_name} Siz kanalga agza boldiniz "
        )

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
