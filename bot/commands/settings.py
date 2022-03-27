from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, \
    InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, KeyboardButtonPollType


async def settings_command(message: types.Message):
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text="Яндекс",
        url="yandex.ru"
    )
    # settings_markup.button(
    #     text="pay",
    #     pay = True
    # )
    settings_markup.button(
        text="помощь",
        callback_data="help"
    )
    await message.answer("Настройки", reply_markup=settings_markup.as_markup())