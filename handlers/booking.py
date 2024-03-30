from aiogram import Router
from handlers.states import Booking
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.simple_row import make_row_keyboard
from datetime import datetime,date,timedelta
from time_module import get_date_list
from texts import txt_booking
from db.reg import get_data
from utils.lst_work import to_times
router = Router()


@router.message(Command("booking"))
async def day(message: Message, state: FSMContext):
    mess = await message.answer(
        text=txt_booking.start,
        reply_markup = make_row_keyboard([i for i in get_date_list(n=7)],1)
        )
    await state.update_data(mess=mess)
    await state.set_state(Booking.choosing_day)

@router.callback_query(Booking.choosing_day)
async def time(message: Message, state: FSMContext):
    data = await state.get_data()
    mess = data.get("mess")
    lst = await get_data(day)
    lst = await to_times(lst)
    print(lst)
    await mess.edit_text(
        text=txt_booking.state.get(Booking.choosing_day._state),
        reply_markup  = make_row_keyboard(lst,1)
    )
    await state.set_state(Booking.choosing_time)

# @router.callback_query(lambda x: x.data in ["Да","Нет"])
# @router.message(Register.confirm_email)
# async def confirm(message: Message, state: FSMContext):
#     data = await state.get_data()
#     mess = data.get("mess","None")
#     print(message.data)
#     if message.data == "Да":
#         data = await state.get_data()
#         email = data.get("chosen_email","None")
#         token = await generate_token(message.from_user.id,email)
#         try:
#             await send_mail(email,token)
#         except:
#             pass
#         await state.update_data(token=token)
#         await mess.edit_text(
#             text=txt_register.state.get(Register.confirm_email._state),
#         )
#         await state.set_state(Register.succsessed)
#     else:
#         await state.set_state(Register.choosing_email)
#         await mess.edit_text(
#             text=txt_register.start,
#         )
        

# @router.message(Register.succsessed)
# async def confirm(message: Message, state: FSMContext):
#     data = await state.get_data()
#     mess = data.get("mess","None")
#     email = data.get("chosen_email","None")
#     token_saved = data.get("token","None")
#     if token_saved == message.text and decode_token(token_saved):
#         status = await register_user(email,str(message.from_user.id))
#     await mess.edit_text(
#         text=txt_register.state.get(Register.succsessed._state),
#     )
#     await state.clear()
#     await state.set_data({})


