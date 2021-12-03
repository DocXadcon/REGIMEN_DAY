import logging
from utils.db_api import db_gino
from aiogram.dispatcher import FSMContext
from aiogram.types import user, message, ReplyKeyboardRemove
from apscheduler import schedulers
from aiogram import Dispatcher, types
from aiogram import executor


from loader import scheduler
from loader import dp
from loader import db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from datetime import datetime
from data import config
from aiogram import types
from utils.db_api import quic_commands as commands
import datetime


async def send_regimen(dp: Dispatcher):
    count_users = await commands.count_users()
    today_day = datetime.datetime.today().weekday()
    for idi in range(1, count_users + 1):
        user95 = await commands.select_user_number(id=idi)
        telegram_idi = user95.telegram_id
        user_time = user95.regimen_time
        hour_now = datetime.datetime.now().hour
        regimen_to_day = ""
        photo_on_day = ""
        if today_day == 0 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_monday
            photo_on_day = "https://i.pinimg.com/originals/40/d4/b1/40d4b154105cef691f6b10cf8c33bb15.jpg"
        elif today_day == 1 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_tuesday
            photo_on_day = "https://i.pinimg.com/736x/2f/0e/b2/2f0eb29458a155ce89094ece237aea3b.jpg"
        elif today_day == 2 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_wednesday
            photo_on_day = "https://i.pinimg.com/originals/7d/6c/93/7d6c93b3c95e252db0e658065ba7bd11.jpg"
        elif today_day == 3 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_thursday
            photo_on_day = "https://i.pinimg.com/originals/73/73/bc/7373bc97c46ce581b8964d4e7b48d12c.jpg"
        elif today_day == 4 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_friday
            photo_on_day = "https://i.pinimg.com/736x/b6/4e/e5/b64ee566b393753f8ee9516664887897.jpg"
        elif today_day == 5 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_saturday
            photo_on_day = "https://i.pinimg.com/originals/20/15/a7/2015a714010624271aad9ba55b8b97fb.jpg"
        elif today_day == 6 and hour_now == user_time:
            regimen_to_day = user95.regimen_on_sunday
            photo_on_day = "https://pbs.twimg.com/media/DrsThuSV4AEmANy.jpg"
        await dp.bot.send_photo(telegram_idi,
                                photo=photo_on_day,
                                caption=f"<b>Твой режим на сегодня😊</b>\n"
                                        f"{regimen_to_day}",
                                reply_markup=ReplyKeyboardRemove())


def schedule_jobs():
    scheduler.add_job(send_regimen, "interval", minutes=1, start_date="2021-12-03 12:00:00",
                      end_date="2022-12-03 12:00:00", args=(dp,))


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db_gino.on_startup(dp)
    logging.info("Создаем таблицу пользователей")
    # await db.gino.drop_all()
    await db.gino.create_all()
    logging.info("Готово")
    await on_startup_notify(dispatcher)
    schedule_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
