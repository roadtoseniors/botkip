from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_FIO = State()
    GET_OPI = State()
    GET_BEST = State()
    GET_NONRAV = State()
    GET_CHANGE = State()
