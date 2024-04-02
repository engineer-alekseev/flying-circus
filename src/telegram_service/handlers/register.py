from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from handlers.states import Register
from aiogram.types import Message
from keyboards.simple_row import make_yn_keyboard
from texts import txt_register
from utils.mail import send_mail
from tokenlib import * 
from db.reg import register_user, info_user


router = Router()

@router.message(Command("register"))
async def cmd_reg(message: Message, state: FSMContext):
    await state.clear()
    await state.set_data({})
    # info = await info_user(str(message.from_user.id))
    # if info[1] == 200:
    #     mess = await message.answer(
    #         text="Вы уже зарегистрированы /register",
    #     )
    #     return None
    mess = await message.answer(
        text=txt_register.start,
        )
    await state.update_data(mess=mess)
    await state.set_state(Register.choosing_email)

@router.message(Register.choosing_email)
async def email(message: Message, state: FSMContext):
    await state.update_data(chosen_email=message.text.lower())
    data = await state.get_data()
    mess = data.get("mess","None")
    await mess.edit_text(
        text=txt_register.state.get(Register.choosing_email._state),
        reply_markup  = make_yn_keyboard()
    )
    await state.set_state(Register.confirm_email)

@router.callback_query(Register.confirm_email)
async def confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    mess = data.get("mess","None")
    if message.data == "Да":
        data = await state.get_data()
        email = data.get("chosen_email","None")
        token = await generate_token(message.from_user.id,email)
    
        code = await send_mail(email,token)
        if code ==201:
            await state.update_data(token=token)
            await mess.edit_text(
                text=txt_register.state.get(Register.confirm_email._state) + f"\n\n{code}",
            )
            await state.set_state(Register.succsessed)
        
    else:
        await state.set_state(Register.choosing_email)
        await mess.edit_text(
            text=txt_register.start,
        )
        
@router.message(Register.succsessed)
async def confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    mess = data.get("mess","None")
    email = data.get("chosen_email","None")
    token_saved = data.get("token","None")
    if token_saved == message.text and decode_token(token_saved):
        status = await register_user(email,str(message.from_user.id))
    await mess.edit_text(
        text=txt_register.state.get(Register.succsessed._state),
    )
    await state.clear()
    await state.set_data({})
