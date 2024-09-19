import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.admin import admin
from app.user import user

load_dotenv()
token = os.getenv("API")


async def main():
   dp = Dispatcher()
   bot = Bot(token=token)
   dp.include_routers(user,admin)
   await dp.start_polling(bot)


if __name__ == '__main__':
   try:
      asyncio.run(main())
   except KeyboardInterrupt:
      print("exit")
