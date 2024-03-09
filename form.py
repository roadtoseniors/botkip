from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ex1.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем опрос.\n Введите свое ФИО')
    await state.set_state(StepsForm.GET_FIO)

async def get_opi(message: Message, state: FSMContext):
    await message.answer(f'Понравился ли вам День открытых дверей?')
    await state.set_state(StepsForm.GET_OPI)
async def get_best(message: Message, state: FSMContext):
    await message.answer(f'Что больше всего вам понравилось в этом мероприятии?')
    await state.set_state(StepsForm.GET_BEST)

async def get_nonrav(message: Message, state: FSMContext):
    await message.answer(f'Что вам не понравилось в проведении Дня открытых Дверей?')
    await state.set_state(StepsForm.GET_NONRAV)

async def get_change(message: Message, state: FSMContext):
    await message.answer(f'Что по вашему мнению нужно поменять в проведении Дня открытых дверей?')
    await state.set_state(StepsForm.GET_CHANGE)