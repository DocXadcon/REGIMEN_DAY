from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery, Update, ReplyKeyboardRemove, message
import asyncpg.exceptions
from data.week import week
from keyboards.inline.Days_of_week import choice_on_morning_time, choose_day_week, choose_new_time
from keyboards.inline.Days_of_week import keyboard_constructor_day
from keyboards.inline.call_back_week import week_callback
from loader import dp, db
from states.Week_states import ChangeDay
from aiogram.dispatcher import FSMContext
from states import Week
from utils.db_api import quic_commands as commands


@dp.message_handler(Command("change_regimen"))
async def send_message(message: types.Message):
    await message.answer(text="<b>Выбери день недели, в котором</b>\n"
                              "<b>хочешь изменить режим👇</b>",
                         reply_markup=choose_day_week
                         )
    await ChangeDay.ChooseDay.set()


@dp.message_handler(state=ChangeDay.ChooseDay)
async def send_text(message: types.Message, state: FSMContext):
    day_of_the_week = message.text
    result = ""
    user = await commands.select_user(telegram_id=message.from_user.id)
    if day_of_the_week == "Понедельник":
        result = user.regimen_on_monday
    elif day_of_the_week == "Вторник":
        result = user.regimen_on_tuesday
    elif day_of_the_week == "Среда":
        result = user.regimen_on_wednesday
    elif day_of_the_week == "Четверг":
        result = user.regimen_on_thursday
    elif day_of_the_week == "Пятница":
        result = user.regimen_on_friday
    elif day_of_the_week == "Суббота":
        result = user.regimen_on_saturday
    elif day_of_the_week == "Воскресенье":
        result = user.regimen_on_sunday
    await message.answer(f"<b>Сейчас твой режим дня выглядит так:</b>\n"
                         f"{result}", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"<b>Напиши новый режим</b>😊")
    await state.update_data(day=day_of_the_week)
    await ChangeDay.NewRegimen.set()


@dp.message_handler(state=ChangeDay.NewRegimen)
async def enter_regimen(message: types.Message, state: FSMContext):
    data = await state.get_data()
    day = data.get("day")
    telegram_id = message.from_user.id
    new_regimen = message.text
    if day == "Понедельник":
        await commands.update_regimen_on_monday(telegram_id, new_regimen)
    elif day == "Вторник":
        await commands.update_regimen_on_tuesday(telegram_id, new_regimen)
    elif day == "Среда":
        await commands.update_regimen_on_wednesday(telegram_id, new_regimen)
    elif day == "Четверг":
        await commands.update_regimen_on_thursday(telegram_id, new_regimen)
    elif day == "Пятница":
        await commands.update_regimen_on_friday(telegram_id, new_regimen)
    elif day == "Суббота":
        await commands.update_regimen_on_saturday(telegram_id, new_regimen)
    elif day == "Воскресенье":
        await commands.update_regimen_on_sunday(telegram_id, new_regimen)

    # user = await commands.select_user(telegram_id=message.from_user.id)
    await message.answer(f"<i><b>Теперь ты будешь получать\n новый режим дня!</b></i>\n"
                         f"<b>Выбери время, в которое утром\n"
                         f"будет приходить режим на день</b>",
                         reply_markup=choice_on_morning_time)
    await ChangeDay.NewTime.set()


@dp.message_handler(state=ChangeDay.NewTime)
async def enter_time(message: types.Message, state: FSMContext):
    result_about_time = int(message.text[0])
    await commands.update_time(message.from_user.id, result_about_time)
    await message.answer(text="<b>Данные были успешно обновлены😉</b>",
                         reply_markup=ReplyKeyboardRemove())
    await state.reset_state(with_data=True)
