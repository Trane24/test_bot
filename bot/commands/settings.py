from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, \
    InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, KeyboardButtonPollType

from bot.commands.callback_data import TestCallbackData


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
        # callback_data="help"
        callback_data=TestCallbackData(text="Hi", user_id=message.from_user.id)
    )
    await message.answer("Настройки", reply_markup=settings_markup.as_markup())


async def settings_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    await call.message.answer(callback_data.text + " " + str(callback_data.user_id))
