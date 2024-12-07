from aiogram import Router, types
from aiogram.filters import Command
from random import choice


info_router = Router()
random_router = Router()


names_array = ["isa", "kamila", "nurs", "adilet", "aya", "islam", "sanjar"]


@info_router.message(Command("myinfo"))
async def info_handler(message: types.Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    answer = f"id: {id}\nИмя: {first_name}\nНик: {username}"
    await message.answer(answer)
    

@random_router.message(Command("random"))
async def random_haddler(message: types.Message):
    random_name = choice(names_array)
    await message.answer(f"Рандомное имя: {random_name}")