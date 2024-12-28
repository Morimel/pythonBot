from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import dotenv_values

from bot_config import database

food_management_router = Router()
# food_management_router.message.filter(F.from_user.id == dotenv_values(".env")["ADMIN_ID"])

class Food(StatesGroup):
    name = State()
    price = State()
    weight = State()
    description = State()
    photo = State()
    category = State()

@food_management_router.message(Command("newdish"))
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
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Введите описание блюда")
    await state.set_state(Food.description)

@food_management_router.message(Food.description)
async def process_photo_request(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отправьте фото блюда")
    await state.set_state(Food.photo)

@food_management_router.message(Food.photo, F.photo)
async def process_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id
    await state.update_data(photo=file_id)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="супы"), KeyboardButton(text="вторые блюда")],
            [KeyboardButton(text="горячие напитки"), KeyboardButton(text="холодные напитки")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Выберите категорию блюда", reply_markup=keyboard)
    await state.set_state(Food.category)

@food_management_router.message(Food.category)
async def process_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()
    print(data)
    database.save_dishes(data)
    await message.answer("Блюдо сохранено!", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@food_management_router.message(Command("dishes"))
async def show_all_dishes(message: types.Message):
    dishes = database.get_all_dishes()
    # Если список блюд пуст
    if not dishes:
        await message.answer("Список блюд пуст.")
        return
    for dish in dishes:
        photo = dish['photo']
        txt = f"Название: {dish['name']}\nЦена: {dish['price']}"
        await message.answer_photo(
            photo=photo,
            caption=txt
        )
