from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command("myinfo"))
async def info_handler(message: types.Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    answer = f"id: {id}\nИмя: {first_name}\nНик: {username}"
    await message.answer(answer)
    

