from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from db.reg import info_user
import json

router = Router()

@router.message(Command("info"))
async def cmd_reg(message: Message, state: FSMContext):
    data = await info_user(str(message.from_user.id))
    if data[1]==200:
        data = json.loads(data[0])
        await message.answer(
            text = '\n'.join(f"{i}: {data[i]}" for i in data),
        )
    else:
        await message.answer(
            text = "Необходима регистрация /register",
        )


@router.message(Command("id"))
async def cmd_reg(message: Message, state: FSMContext):
    await message.answer(
        f'Ваш Телеграмм ID: {message.from_user.id}',
        )
