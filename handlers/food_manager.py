from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot_config import database

food_management_router = Router()

class Food(StatesGroup):
    name = State()
    price = State()
    weight = State()


@food_management_router.message(Command("newfood"))
async def create_new_food(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда")
    await state.set_state(Food.name)
    
@food_management_router.message(Food.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену блюда")
    await state.set_state(Food.price)
    
@food_management_router.message(Food.price)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Введите вес блюда")
    await state.set_state(Food.weight)

@food_management_router.message(Food.weight)
async def process_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(data)
    database.save_food(data)
    await message.answer("Блюдо сохранено")
    await state.clear()