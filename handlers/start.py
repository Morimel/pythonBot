from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from handlers.review_dialog import RestourantReview  
from handlers.food_manager import Food


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")],
            [types.InlineKeyboardButton(text="Добавить блюдо", callback_data="newfood")]
        ]
    )
    await message.answer(f"Привет, {name}!", reply_markup=kb)

@start_router.callback_query(F.data == "review")
async def review_button(callback: types.CallbackQuery, state: FSMContext):
    did_review = False
    
    if did_review == False:
        did_review = True
        # Переводим пользователя в состояние RestourantReview.name
        await callback.message.answer("Как вас зовут?")
        await state.set_state(RestourantReview.name)
        await callback.answer()
    elif did_review == True:
        await callback.message.answer("Опрос можно пройти только один раз")
        
@start_router.callback_query(F.data == "newfood")
async def newfood_button(callback: types.CallbackQuery, state: FSMContext):
    # Переводим пользователя в состояние RestourantReview.name
    await callback.message.answer("Введите название блюда")
    await state.set_state(Food.name)
    await callback.answer()
        