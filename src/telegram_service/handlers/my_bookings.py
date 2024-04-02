from aiogram import Router
from handlers.states import My_bookings
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.simple_row import make_row_keyboard
from datetime import datetime,date,timedelta
from db.book import get_bookings_by_user,del_booking
from aiogram.filters import Command
from db.reg import info_user
router = Router()


@router.message(Command("my_bookings"))
async def room_sel(message: Message, state: FSMContext):
    info = await info_user(str(message.from_user.id))
    if info[1] == 401:
        mess = await message.answer(
            text="Необходима регистрация /register",
        )
        return None
    lst = await get_bookings_by_user(message.from_user.id)
    lst = list(map(lambda x: x["start_time"].replace('T',' ')[:-3]+" - "+x["end_time"].replace('T',' ')[:-3] + f"!{x['id']}",lst))
    if lst:
        mess = await message.answer(
        text="ваши бронировки, выберите:",
        reply_markup = make_row_keyboard(lst,1,spl = True)
        )
    else:
        mess = await message.answer(
        text="Ничего не забронировано",
        )
    await state.update_data(mess=mess)
    await state.set_state(My_bookings.choosing_booking)

@router.callback_query(My_bookings.choosing_booking)
async def date_sel(message: Message, state: FSMContext):
    b_id = message.data
    await state.update_data(b_id=b_id)
    data = await state.get_data()
    mess = data.get("mess")
    mess = await mess.edit_text(
        text="Что делаем?",
        reply_markup = make_row_keyboard(['Удалить','Отмена'],1)
        )
    await state.set_state(My_bookings.confirm)

@router.callback_query(My_bookings.confirm)
async def date_sel(message: Message, state: FSMContext):
    data = await state.get_data()
    mess = data.get("mess")
    b_id = data.get("b_id")
    if message.data == 'Удалить':
        
        status = await del_booking(b_id,message.from_user.id)
        mess = await mess.edit_text(
            text=f"Готово \n{status}",
        )
    else:
        await mess.delete()
    await state.clear()
    await state.set_data({})

