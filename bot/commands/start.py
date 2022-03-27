from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, \
    InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, KeyboardButtonPollType


async def start(message: types.Message) -> None:
    #3 способа создания кнопки
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text="Помощь"
    )

    menu_builder.add(
        KeyboardButton(text="Отправить контакт", request_contact=True)
    )

    menu_builder.row(
        KeyboardButton(text="Отправить голосование", request_poll=KeyboardButtonPollType())
    )

    await message.answer(
        "hello",
        #2 способоа
        reply_markup=menu_builder.as_markup(resize_keyboard = True)
        #reply_markup=ReplyKeyboardMarkup(keyboard=menu_builder.export())

    )
