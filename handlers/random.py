from aiogram import Router, types
from aiogram.filters import Command
from random import choice

random_router = Router()

names_array = ["isa", "kamila", "nurs", "adilet", "aya", "islam", "sanjar"]


@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    random_name = choice(names_array)
    await message.answer(f"Рандомное имя: {random_name}")