from aiogram import Bot, Dispatcher, executor, types
from cfg import TOKEN_API


HELP_COMMAND="""
/help - command list
/start - start work with this bot"""

bot=Bot(TOKEN_API)
dp=Dispatcher(bot)



@dp.message_handler(commands=['help'])
async def help_command(mesage: types.Message):
    await mesage.answer(text=HELP_COMMAND)
    await mesage.delete()


@dp.message_handler(commands=['start'])
async def help_command(mesage: types.Message):
    await mesage.answer(text="work started")
    await mesage.delete()


@dp.message_handler(text=('да'))
async def process_start_command(message: types.Message):
   await message.answer('пизда')

@dp.message_handler(text=('Да'))
async def process_start_command(message: types.Message):
   await message.answer('пизда')

@dp.message_handler(text=('ДА'))
async def process_start_command(message: types.Message):
   await message.answer('пизда')

@dp.message_handler(text=('Da'))
async def process_start_command(message: types.Message):
   await message.answer('пизда')


@dp.message_handler(text=('ты ебалан?'))
async def process_start_command(message: types.Message):
   await message.answer('а может ты?' + ' 🦃')
   
@dp.message_handler(text=('Ты еблан?'))
async def process_start_command(message: types.Message):
   await message.answer('а может ты?' + ' 🦃')

@dp.message_handler(text=('Ты ебалан?'))
async def process_start_command(message: types.Message):
   await message.answer('а может ты?' + ' 🦃')

@dp.message_handler(text=('ты еблан?'))
async def process_start_command(message: types.Message):
   await message.answer('а может ты?' + ' 🦃')

if __name__ == '__main__':
    executor.start_polling(dp)
