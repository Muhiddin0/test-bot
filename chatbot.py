import requests
import json

import logging

from pprint import pprint
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6384385753:AAHv0UeCOMIssdV9ufo9qlaB1gE-ojxJ8K4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def func(message:types.Message):
  text = message.text
  
  url = "https://twitter.blueto.app:8443/cargpt/sendPrompt"

  payload = json.dumps({
    "app": "com.dominapp.supergpt",
    "deviceId": "4e2a3d23384a4dfc",
    "email": "mkabraliev2005@gmail.com",
    "isPremiumUser": False,
    "isProUser": False,
    "page": 0,
    "proUserId": "",
    "proUserToken": "",
    "text": text,
    "token": "4e2a3d23384a4dfc"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload).json()

  if response['textResponse']:  
    await message.answer(text=response['textResponse'])
  else:
    await message.answer(text="Kechirasiz siz izlagan ma'lumot topilmadi 🔍")
  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)