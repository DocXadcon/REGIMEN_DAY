from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery, Update, ReplyKeyboardRemove, message
import asyncpg.exceptions
from data.week import week
from keyboards.inline.Days_of_week import choice_on_morning_time
from keyboards.inline.Days_of_week import keyboard_constructor_day
from keyboards.inline.call_back_week import week_callback
from loader import dp, db
from aiogram.dispatcher import FSMContext
from states import Week
from loader import scheduler
from datetime import datetime, date
from utils.db_api import quic_commands as commands


# async def take_telegram_id(mes: types.Message):
#     return mes.from_user.id
#
#
# async def send_regimen_on_monday(dp: Dispatcher):
#     info_user = await db.select_user(telegram_id=take_telegram_id())
#     go1 = list(info_user)


@dp.message_handler(Command("create_regimen"))
async def send_calendar(message: types.Message):
    await message.answer_photo(
        photo='https://3schoolnm.ru/images/2020-2021/news/aprel/6apr/qQ_8_oiOzW4.jpg',
        caption=f"{message.from_user.full_name}, <b>давай начнём заполнять!</b>"
    )
    await message.answer_photo(
        photo='https://i.pinimg.com/originals/b9/78/6e/b9786edf77a1c77f4c52ff05b5c76c5e.jpg',
        reply_markup=keyboard_constructor_day(name_day="Понедельник", item_id=week["Понедельник"])
    )


@dp.callback_query_handler(week_callback.filter())
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>понедельник</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Monday.set()


@dp.message_handler(state=Week.Monday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer1 = message.text
    await state.update_data(answer1=answer1)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_photo(
        photo='https://i.ytimg.com/vi/HZMA9TCE_1M/hqdefault.jpg',
        reply_markup=keyboard_constructor_day(name_day="Вторник", item_id=week["Вторник"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Monday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>вторник</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Tuesday.set()


@dp.message_handler(state=Week.Tuesday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer2 = message.text
    await state.update_data(answer2=answer2)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_animation(
        animation='https://thumbs.gfycat.com/SnarlingPitifulIbex-max-1mb.gif',
        reply_markup=keyboard_constructor_day(name_day="Среда", item_id=week["Среда"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Tuesday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>среду</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Wednesday.set()


@dp.message_handler(state=Week.Wednesday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer3 = message.text
    await state.update_data(answer3=answer3)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_animation(
        animation='https://thumbs.gfycat.com/LastGargantuanIslandwhistler-size_restricted.gif',
        reply_markup=keyboard_constructor_day(name_day="Четверг", item_id=week["Четверг"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Wednesday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>четверг</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Thursday.set()


@dp.message_handler(state=Week.Thursday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer4 = message.text
    await state.update_data(answer4=answer4)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_animation(
        animation='https://data.whicdn.com/images/294369169/original.gif',
        reply_markup=keyboard_constructor_day(name_day="Пятница", item_id=week["Пятница"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Thursday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>пятницу</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Friday.set()


@dp.message_handler(state=Week.Friday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer5 = message.text
    await state.update_data(answer5=answer5)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_photo(
        photo='https://thumbs.gfycat.com/NiceThoseGalapagosdove-mobile.jpg',
        reply_markup=keyboard_constructor_day(name_day="Суббота", item_id=week["Суббота"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Friday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>субботу</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Saturday.set()


@dp.message_handler(state=Week.Saturday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer6 = message.text
    await state.update_data(answer6=answer6)
    await message.answer(text="<pre>Отлично! Идем дальше!</pre>")
    await message.answer_animation(
        animation='https://www.picgifs.com/graphics/s/sunday/graphics-sunday-111047.gif',
        reply_markup=keyboard_constructor_day(name_day="Воскресенье", item_id=week["Воскресенье"])
    )


@dp.callback_query_handler(week_callback.filter(), state=Week.Saturday)
async def write_on_monday(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_caption(caption="<i>Напиши ниже все </i>"
                                            "<i>необходимые дела на <u><b>воскресенье</b></u> </i>"
                                            "<i>одним сообщением📲</i>")
    await Week.Sunday.set()


@dp.message_handler(state=Week.Sunday)
async def send_calendar(message: types.Message, state: FSMContext):
    answer7 = message.text
    telegram_id = message.from_user.id
    await state.update_data(answer7=answer7)
    await message.answer(text="<b>Отлично! Режим дня на неделю готов</b>\n"
                              "<b>Во сколько часов утром отправлять тебе дела на день?</b>",
                         reply_markup=choice_on_morning_time)

    await Week.Choice_time.set()


@dp.message_handler(state=Week.Choice_time)
async def all_days(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")
    answer5 = data.get("answer5")
    answer6 = data.get("answer6")
    answer7 = data.get("answer7")
    telegram_id = message.from_user.id
    await state.update_data(user_id=telegram_id)
    answer_time = int(message.text[0])
    await message.answer(text=f"<b>Ты будешь получать свой режим утром\n"
                              f"в {answer_time} утра\n"
                              f"Чтобы изменить режим\n"
                              f"используй команду - </b>/change_regimen",
                         reply_markup=ReplyKeyboardRemove())
    await commands.update_regimen_on_week(
        telegram_id=message.from_user.id,
        regimen_on_monday=answer1,
        regimen_on_tuesday=answer2,
        regimen_on_wednesday=answer3,
        regimen_on_thursday=answer4,
        regimen_on_friday=answer5,
        regimen_on_saturday=answer6,
        regimen_on_sunday=answer7,
        regimen_time=answer_time)
    await state.reset_state(with_data=False)









#         "\n".join(
#             [
#                 f"Привет, {message.from_user.full_name}!",
#                 f"Ты был занесен в базу",
#                 f"В базе <b>{count_users}</b> пользователей",
#                 "",
#                 # f"<code>User: {username} - {full_name}",
#                 # f"{user_data=}",
#                 # f"{user_data_dict=}</code>"
#             ]
#         ),
#         reply_markup=ReplyKeyboardRemove()
#
#     )
#     await state.reset_state(with_data=False)
#     # info_user = await db.select_user(telegram_id=message.from_user.id)
#     # go1 = list(info_user)
#     # telegram_id95 = db.users[0].get("full_name")
#     # list_telegram_id = list(telegram_id95)
#     # await message.answer(text=f"{telegram_id95}")
#     # async def send_message_to_admin(dp: Dispatcher):
#     #     telegram_id = db.select_user("telegram_id")
#     #     await dp.bot.send_photo(telegram_id,
#     #                             photo="https://i.pinimg.com/originals/40/d4/b1/40d4b154105cef691f6b10cf8c33bb15.jpg",
#     #                             caption="Сообщение по таймеру")
#
#
# async def send_regimen_on_monday1():
#     # data95 = await state.get_data()
#     # telegram_id = data95.get("user_id")
#     data_user = await db.select_user(telegram_id=2013616621)
#     data_user = dict(data_user)
#     text = "Hello world"
#     return data_user
