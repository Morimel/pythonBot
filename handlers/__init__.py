from aiogram import Router, F

from .start import start_router
from .review_dialog import review_router
from .picture import picture_router
from .info import info_router
from .random import random_router
from .dishes import food_management_router

private_router = Router()


private_router.include_router(start_router)
private_router.include_router(review_router)
private_router.include_router(picture_router)
private_router.include_router(info_router)
private_router.include_router(random_router)
private_router.include_router(food_management_router)

private_router.message.filter(F.chat.type == "private")
private_router.callback_query.filter(F.chat.type == "private")