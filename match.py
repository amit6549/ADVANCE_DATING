from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text.lower() == "find match")
async def find_match(message: types.Message):
    # Placeholder - query DB for suitable match
    await message.answer("🔍 Searching for potential matches near you...")
