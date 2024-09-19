from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Сұрақ қою.")]
],
resize_keyboard=True,
input_field_placeholder="Cұрақ қою үшін батырманы басыңыз!")


inline_main = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Қайта сұрақ қою.", callback_data="send_again_message")]
])