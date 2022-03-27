__all__ = ["register_user_commands", "bot_commands"]

from aiogram import Router, F
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.command import CommandStart

from bot.commands.start import start
from bot.commands.help import help_command, help_func, call_help_func
from bot.commands.settings import settings_command

def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(start, F.text == "Старт")
    router.message.register(help_func, F.text == "Помощь")
    router.message.register(settings_command, Command(commands=["settings"]))

    router.callback_query.register(call_help_func, F.data == "help")