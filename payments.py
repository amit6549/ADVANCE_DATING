from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text.lower() == "buy stars")
async def buy_stars(message: types.Message):
    await message.answer("To buy stars 💫, send crypto to this Binance address:\n...")
