from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text.lower() == "edit profile")
async def edit_profile(message: types.Message):
    await message.answer("Send me your bio and what you're looking for.")
