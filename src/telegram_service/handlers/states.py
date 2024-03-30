from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    choosing_email = State()
    confirm_email = State()
    succsessed = State()

class Booking(StatesGroup):
    choosing_day = State()
    choosing_time = State()
    choosing_room = State()

class Booking_remove(StatesGroup):
    choosing_booking = State()
    confirm = State()

# a = Booking()
# print(a.choosing_day._state)
# for i in Booking.__dict__:
#     if not i.startswith('__'):
#         print(i)