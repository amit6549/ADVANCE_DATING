from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.database import models

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("👋 Welcome to LoveLink! Let’s set up your profile.")
