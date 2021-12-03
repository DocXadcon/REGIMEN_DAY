from webbrowser import get

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Update

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Список команд:</b>",
            "/create_regimen - Создать режим дня",
            "/change_regimen - Изменить режим дня",
            "/help - Получить справку"
            )

    await message.answer("\n".join(text))
