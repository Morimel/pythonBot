import asyncio

from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.info import info_router
from handlers.random import random_router
from handlers.review_dialog import review_router
from handlers.food_manager import food_management_router

async def on_startup(bot):
    database.create_tables()
    print("Таблица review_table успешно создана или уже существует.")

async def main():
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(picture_router)
    dp.include_router(info_router)
    dp.include_router(random_router)
    dp.include_router(food_management_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())