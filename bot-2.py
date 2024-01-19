import requests

import logging

from pprint import pprint
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6384385753:AAHv0UeCOMIssdV9ufo9qlaB1gE-ojxJ8K4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 3 - AUDIO
@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def func(message:types.Message):
  file_id = message.audio.file_id
  url = "https://api.telegram.org/bot{}/getFile?file_id={}".format(API_TOKEN, file_id)

  request = requests.get(url).json()
  file_path = request['result']['file_path']

  source_url = "https://api.telegram.org/file/bot{}/{}".format(API_TOKEN, file_path)

  await message.answer(source_url)



# 4 - PHOTO
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def func(message:types.Message):
  message.photo[0].file_id
  await message.answer('4 - PHOTO')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)