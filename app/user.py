from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from app.state import Request
from app.ai import get_response
from aiogram.enums import ChatAction
from app.keyboards import main, inline_main
from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("API")
user = Router()
bot = Bot(token=token)

limit = {}

@user.message(CommandStart())
async def cmd_start(message: Message):
   user_name = message.from_user.full_name
   await message.answer(f'Сәлем {user_name}! Мен сенің сұрақтарыңа жауап беруші ботпын!',
                        reply_markup=main)
   await bot.send_message(1894986937, f'{message.from_user.full_name}: started!')
   user_id = str(message.from_user.id)+message.from_user.full_name
   limit[user_id] = 0



@user.callback_query( F.data == 'send_again_message')
async def cmd_start(callback: CallbackQuery, state: FSMContext):
   await state.set_state(Request.text)
   await callback.message.answer("Маған қалаған сұрағыңызды қойыңыз!")
   


@user.message(F.text == 'Сұрақ қою.')
async def cmd_start(message: Message, state:FSMContext):
   await state.set_state(Request.text)
   await message.answer("Маған қалаған сұрағыңызды қойыңыз!")




@user.message(Request.text)
async def response(message: Message, state: FSMContext):
   await message.bot.send_chat_action(chat_id=message.from_user.id,
                                      action=ChatAction.TYPING)
   user_id = str(message.from_user.id)+message.from_user.full_name
   if limit[user_id] < 10:
      await message.answer(text="Сізде сұрақ қою мүмкіндігі жоқ! Сіз лимиттен асып кеттіңіз!")
   else:
      request = message.text + " answer in kazakh language!"
      try:
         rspn = await get_response(request=request)
      except:
         rspn = "Сізде сұрақ қою мүмкіндігі жоқ!"
      await message.answer(text = rspn)
      limit[user_id]+=1
      await message.answer(text= "Тағы сұрақ болса батырманы бас!", reply_markup=inline_main)
        
      await bot.send_message(1894986937, f'{message.from_user.full_name}: {message.text}')
   await state.clear()





