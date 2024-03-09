import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import form
from ex1.statesform import StepsForm
logging.basicConfig(level=logging.INFO)
bot = Bot(token="6657561174:AAGPcs335hPHmEh_V_VIZsGi0Dv6dfkoZcE")
dp = Dispatcher()
dp.message.register(form.get_form, Command(commands='form'))
dp.message.register(form.get_name, StepsForm.GET_FIO)
dp.message.register(form.get_opi, StepsForm.GET_OPI)
dp.message.register(form.get_best, StepsForm.GET_BEST)
dp.message.register(form.get_nonrav, StepsForm.GET_NONRAV)
dp.message.register(form.get_change, StepsForm.GET_CHANGE)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("form"))
async def cmd_start(message: types.Message):
    await message.answer(form)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())