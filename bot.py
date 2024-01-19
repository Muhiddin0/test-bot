import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6384385753:AAHv0UeCOMIssdV9ufo9qlaB1gE-ojxJ8K4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 1 - commands
@dp.message_handler(commands=['start', 'help'])
async def func(message:types.Message):
  await message.answer('1-commands')

# 2 - text
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def func(message:types.Message):
  await message.answer(
    text='<b>Salom olam</b>\n <i>italic</i>',
    parse_mode="HTML",
  )

# 3 - AUDIO
@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def func(message:types.Message):
  # with open('audioa.mp3', "rb") as f:
  #   await message.answer_audio(
  #     audio=f
  #   )
  await message.answer_audio(
    audio="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3?_=1",
    caption="salom caption"
  )
  await message.answer('3-AUDIO')

# 4 - PHOTO
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def func(message:types.Message):
  await message.answer('4 - PHOTO')

# 5 - CONTACT
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def func(message:types.Message):
  await message.answer('5 - CONTACT')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)