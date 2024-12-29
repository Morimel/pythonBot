from aiogram import Router, F, types
from aiogram.filters import Command

group_router = Router()
group_router.message.filter(F.chat.type != "private")

BAD_WORDS = ("Дурак", "дурак")

@group_router.message(Command("ban", prefix="!"))
async def ban_user_handler(message: types.Message):
    rpl = message.reply_to_message
    if not rpl:
        await message.answer("The command '!ban' should be reply!")
        return
    author = message.reply_to_message.from_user.id
    await message.ban.ban_chat_member(
        chat_id=message.chat_id,
        user_id=author
    )
    await message.answer("User banned")
    

@group_router.message(F.text)
async def check_bad_words_handler(message: types.Message):
    # await message.answer(f"Привет, {message.from_user.first_name}")
    for word in BAD_WORDS:
        if word in message.text:
            await message.answer("Bad word")
            await message.delete()
            break
    