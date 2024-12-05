import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
names_array = ["isa", "kamila", "nurs", "adilet", "aya", "islam", "sanjar"]

@dp.message(Command("start"))
async def start_haddler(message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}!")
    

@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    answer = f"id: {id}\nИмя: {first_name}\nНик: {username}"
    await message.answer(answer)
    

@dp.message(Command("random"))
async def random_haddler(message):
    random_name = choice(names_array)
    await message.answer(f"Рандомное имя: {random_name}")



async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())