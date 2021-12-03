from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
import asyncpg.exceptions
from utils.db_api import db_gino
from loader import dp
from utils.db_api import quic_commands as commands
from builtins import AttributeError


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b><i>Привет, {message.from_user.full_name}!\n"
                         "Это бот, чтобы создать режим дня на всю неделю!</i></b>\n"
                         "<b>Нажми на эту команду - /create_regimen</b>")

    try:
        user = await commands.add_user(telegram_id=message.from_user.id, name=message.from_user.full_name,
                                       email="dfskljjklfds")
    except asyncpg.exceptions.UniqueViolationError:
        user = await commands.select_user(telegram_id=message.from_user.id)













    # all_users = await commands.select_all_users()
    # one_user = await commands.select_user(id=message.from_user.id)
    # print(f"This user - {one_user}")
    # print(f"Все пользователи - {all_users}")
    # await message.answer(f"{all_users}")
    # user = await commands.select_user(telegram_id=message.from_user.id)
    # users = await commands.select_all_users()
    # await message.answer(text=f"{user.telegram_id}\n")
#                           f"{user.name}\n"
#                           f"{user.email}\n"
#                           f"{user.regimen_on_monday}")
# await message.answer(text=f"{user.id}")
# count_users = await commands.count_users()

# all_users = await commands.select_all_users()
# one_users = [enumerate(start=1)]
# dict99999 = dict(zip(all_users,one_users))
# await message.answer(text=f"{all_users}")
# await message.answer(text=f"{dict99999}")
# await message.answer(text=f"{one_users}")
# count = await commands.count_users()
# first_user1 = await commands.select_user(id=message.from_user.id)
# name95 = await commands.select_user(id=message.from_user.id)
# first_user = first_user1.id
# user_name = first_user.email
# await message.answer(text=f"Base has {count} users"
#                           f"{name95}")
# await message.answer(text=f"{first_user1}")
# await message.answer(text=f"{first_user}")

# await message.answer(text=f"Your name - {user_name}")
# try:
#     user = await db.add_user(
#         full_name=message.from_user.full_name,
#         username=message.from_user.username,
#         telegram_id=message.from_user.id,
#         regimen_on_monday=None,
#         regimen_on_tuesday=None,
#         regimen_on_wednesday=None,
#         regimen_on_thursday=None,
#         regimen_on_friday=None,
#         regimen_on_saturday=None,
#         regimen_on_sunday=None,
#         regimen_time=None
#     )
# except asyncpg.exceptions.UniqueViolationError:
#     user = await db.select_user(telegram_id=message.from_user.id)

# count_users = await db.count_users()
#
# user_data = list(user)
#
# user_data_dict = dict(user)
#
# username = user.get("username")
# full_name = user[1]
#
# await message.answer(
#     "\n".join(
#         [
#             f"Привет, {message.from_user.full_name}!",
#             f"Ты был занесен в базу",
#             f"В базе <b>{count_users}</b> пользователей",
#             "",
#             f"<code>User: {username} - {full_name}",
#             f"{user_data=}",
#             f"{user_data_dict=}</code>"
#         ]
#     ),
#     reply_markup=ReplyKeyboardRemove())
