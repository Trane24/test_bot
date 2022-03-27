from aiogram import types
from aiogram.dispatcher.filters import CommandObject
from aiogram.types import InlineKeyboardButton

from bot.commands.bot_commands import bot_commands


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f"{cmd[0]} - {cmd[1]} \n\n{cmd[2]}"
                )
        else:
            return await message.answer("комманда ненайдена")
    return help_func(message)
    # return await message.answer("помощь по боту, юзай /help")


async def help_func(message: types.Message):
    return await message.answer(
        "Это охуеть кнопка"

    )


async def call_help_func(call: types.CallbackQuery):
    await call.message.edit_text(  # call.message.answer ||| call.answer
        "Это охуеть кнопка",
        reply_markup=call.message.reply_markup#.inline_keyboard.append([InlineKeyboardButton(text="back", callback_data="clear")])
    )

#
# async def clear_call_help_func(call: types.CallbackQuery):
#     await call.message.edit_text(
#
#         "fshfdhserhefhtewh"
#     )
