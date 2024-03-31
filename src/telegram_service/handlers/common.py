from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    builder = ReplyKeyboardBuilder()
    list(map(lambda x: builder.add(KeyboardButton(text=x)),["/register","/cancel","/info","/id","/booking","/my_bookings"]))
    builder.adjust(1)

    await message.answer(
        text="Привет! Выберите действие из меню",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await state.set_data({})
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )