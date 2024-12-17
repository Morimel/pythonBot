from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot_config import database

review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    number = State()
    cleaning = State()
    complaints = State()

@review_router.message(Command("review"))
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)

@review_router.message(RestourantReview.name)
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона или инстаграм")
    await state.set_state(RestourantReview.number)

@review_router.message(RestourantReview.number)
async def craete_keyboard(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    # Создание текстовой клавиатуры
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Плохо"), KeyboardButton(text="Удовлетворительно")],
            [KeyboardButton(text="Хорошо"), KeyboardButton(text="Отлично")]
        ],
        resize_keyboard=True,  # Уменьшение размера кнопок
        one_time_keyboard=True  # Клавиатура исчезает после выбора
    )
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=keyboard)
    await state.set_state(RestourantReview.cleaning)

@review_router.message(RestourantReview.cleaning)
async def process_cleaning(message: types.Message, state: FSMContext):
    await state.update_data(cleaning=message.text)
    await message.answer("Дополнительные комментарии/жалоба?", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RestourantReview.complaints)

@review_router.message(RestourantReview.complaints)
async def process_complaints(message: types.Message, state: FSMContext):
    await state.update_data(complaints=message.text)
    user_data = await state.get_data()
    print("Данные для сохранения:", user_data)
    await message.answer(
        "Спасибо за ваш отзыв!\n\n"
        f"Имя: {user_data.get('name')}\n"
        f"Контакт: {user_data.get('number')}\n"
        f"Чистота: {user_data.get('cleaning')}\n"
        f"Комментарии: {user_data.get('complaints')}"
    )
    database.save_table(user_data)
    # остановка диалога 
    await state.clear()
