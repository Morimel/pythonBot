import asyncio
import logging

from bot_config import dp, bot, database
from handlers import private_router
from handlers.group_managemet import group_router

async def on_startup(bot):
    database.create_tables()
    print("Таблица review_table успешно создана или уже существует.")

async def main():
    dp.include_router(private_router)
    
    dp.startup.register(on_startup)
    dp.startup.register(group_router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())