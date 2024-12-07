from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from random import choice


picture_router = Router()


recipes = [
    {"image": "images/pasta.jpg", "recipe": "Рецепт пасты: 1) Сварите пасту. 2) Приготовьте соус из томатов, чеснока и базилика. 3) Смешайте и подавайте."},
    {"image": "images/stake.jpg", "recipe": "Рецепт стейка: 1) Нагрейте сковороду с маслом до высокой температуры. 2) Посолите и поперчите стейк. 3) Обжарьте с каждой стороны по 2-3 минуты для прожарки медиум. 4) Дайте отдохнуть 5 минут перед подачей."},
    {"image": "images/pizza.jpg", "recipe": "Рецепт пиццы: 1) Приготовьте тесто. 2) Добавьте томатный соус, сыр и начинки. 3) Выпекайте при 200°C в течение 15 минут."}
]


@picture_router.message(Command("picture"))
async def send_random_food(message: types.Message):
    selected_recipe = choice(recipes)
    photo = FSInputFile(selected_recipe["image"])
    recipe_text = selected_recipe["recipe"]
    
    await message.answer_photo(
        photo=photo,
        caption=recipe_text
    )