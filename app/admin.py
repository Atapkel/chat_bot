from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from app.user import limit
from aiogram.filters import Filter

admin = Router()


class AdminProtect(Filter):

   async def __call__(self, message: Message):
        return message.from_user.id == 1894986937
   

@admin.message( AdminProtect(), Command('repo'))
async def repo(message: Message):
    ans = str()
    for k in limit:
        ans += f'{k}: {limit[k]}\n'
    await message.answer(text=ans)

@admin.message(AdminProtect(), Command('zero'))
async def zero(message:Message):
    for k in limit:
        limit[k] = 0
    await message.answer(text="All users zero!")


@admin.message(AdminProtect(), Command('help'))
async def help(message:Message):
    await message.answer(text="Command: repo, zero")