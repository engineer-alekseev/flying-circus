from aiogram import Router
from handlers.states import Booking
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.simple_row import make_row_keyboard
from datetime import datetime,date,timedelta
from time_module import get_date_list
from texts import txt_booking
from db.book import fetch_rooms, book, get_books
from utils.lst_work import to_times

router = Router()


@router.message(Command("booking"))
async def room_sel(message: Message, state: FSMContext):
    lst = await fetch_rooms(message.from_user.id)
    await state.clear()
    await state.set_data({})
    mess = await message.answer(
        text=txt_booking.start,
        reply_markup = make_row_keyboard([f"{i['name']} - {i['location']}" for i in lst],1)
        )
    lst = {f"{i['name']} - {i['location']}" : i for i in lst}
    await state.update_data(mess=mess)
    await state.update_data(lst=lst)
    await state.set_state(Booking.choosing_room)

@router.callback_query(Booking.choosing_room)
async def date_sel(message: Message, state: FSMContext):
    data = await state.get_data()
    room = message.data
    lst = get_date_list(n=7)
    await state.update_data(room=room)
    mess = data.get("mess")
    mess = await mess.edit_text(
        text=txt_booking.state.get(Booking.choosing_day._state),
        reply_markup = make_row_keyboard([i for i in lst],1)
        )
    await state.set_state(Booking.choosing_day)

@router.callback_query(Booking.choosing_day)
async def int_sel(message: Message, state: FSMContext):
    data = await state.get_data()
    day_ = message.data
    await state.update_data(day=day_)
    room = data.get("room")
    lst = data.get("lst")
    room = lst[room]["id"]
    await state.update_data(room=room)
    mess = data.get("mess")
    day =datetime.strptime(message.data,"%A %d %b %Y").strftime("%Y-%m-%d")
    lst = await get_books(room,day,message.from_user.id)
    lst = await to_times(lst)
    mess = await mess.edit_text(
        text=txt_booking.state.get(Booking.choosing_interval._state),
        reply_markup = make_row_keyboard([i for i in lst],1)
        )
    await state.set_state(Booking.choosing_interval)


@router.callback_query(Booking.choosing_interval)
async def start_time(message: Message, state: FSMContext):
    data = await state.get_data()
    interval = message.data
    await state.update_data(interval=interval)
    mess = data.get("mess")
    ans = []
    start, end = interval.split("-")
    start = int(start.split(":")[0])*60+int(start.split(":")[1])
    end = int(end.split(":")[0])*60+int(end.split(":")[1])
    while start < end:
        ans.append(start)
        start+=15
    ans = list(map(lambda x:f"{x//60:0{2}d}:{x%60:0{2}d}",ans))

    await mess.edit_text(
        text=txt_booking.state.get(Booking.choosing__start_time._state),
        reply_markup  = make_row_keyboard(ans,4)
    )
    await state.set_state(Booking.choosing__start_time)

@router.callback_query(Booking.choosing__start_time)
async def start_time(message: Message, state: FSMContext):
    data = await state.get_data()
    interval = data.get("interval")
    start_time =  message.data
    await state.update_data(start_time=start_time)
    mess = data.get("mess")
    ans = []
    end = interval.split("-")[1]
    start = start_time
    start = int(start.split(":")[0])*60+int(start.split(":")[1])
    end = int(end.split(":")[0])*60+int(end.split(":")[1])
    n=0
    while start < end:
        start+=15
        ans.append(start)
        n+=1
        if n==4: break
    ans = list(map(lambda x:f"{start_time}-{x//60:0{2}d}:{x%60:0{2}d}",ans))
    
    await mess.edit_text(
        text=txt_booking.state.get(Booking.choosing__end_time._state),
        reply_markup  = make_row_keyboard(ans,1)
    )
    await state.set_state(Booking.choosing__end_time)

@router.callback_query(Booking.choosing__end_time)
async def start_time(message: Message, state: FSMContext):
    data = await state.get_data()
    interval = message.data
    await state.update_data(start_time=start_time)
    mess = data.get("mess")
    day_ = data.get("day")
    room = data.get("room")
    day_ =datetime.strptime(day_,"%A %d %b %Y").strftime("%Y-%m-%d")
    start,finish = interval.split("-")
    start = f"{day_} {start}"
    finish = f"{day_} {finish}"
    await book(start,finish,room,message.from_user.id)
    await mess.edit_text(
        text=txt_booking.finish,
    )
    await state.clear()
    await state.set_data({})