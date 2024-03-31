from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    choosing_email = State()
    confirm_email = State()
    succsessed = State()

class Booking(StatesGroup):
    choosing_room = State()
    choosing_day = State()
    choosing_interval = State()
    choosing__start_time = State()
    choosing__end_time = State()

class Booking_remove(StatesGroup):
    choosing_booking = State()
    confirm = State()

