from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(telegram_id: int, name: str = None, email: str = None, regimen_on_monday: str = None,
                   regimen_on_tuesday: str = None,
                   regimen_on_wednesday: str = None, regimen_on_thursday: str = None, regimen_on_friday: str = None,
                   regimen_on_saturday: str = None,
                   regimen_on_sunday: str = None, regimen_time: str = None):
    # try:
    user = User(telegram_id=telegram_id, name=name, email=email, regimen_on_monday=regimen_on_monday,
                regimen_on_tuesday=regimen_on_tuesday,
                regimen_on_wednesday=regimen_on_wednesday, regimen_on_thursday=regimen_on_thursday,
                regimen_on_friday=regimen_on_friday, regimen_on_saturday=regimen_on_saturday,
                regimen_on_sunday=regimen_on_sunday, regimen_time=regimen_time)
    await user.create()

    # except UniqueViolationError:
    #     pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(telegram_id: int):
    user = await User.query.where(User.telegram_id == telegram_id).gino.first()
    return user


async def select_user_number(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_regimen_on_week(telegram_id, regimen_on_monday, regimen_on_tuesday,
                                 regimen_on_wednesday, regimen_on_thursday, regimen_on_friday, regimen_on_saturday,
                                 regimen_on_sunday, regimen_time):
    user = await User.get(telegram_id)
    await user.update(regimen_on_monday=regimen_on_monday, regimen_on_tuesday=regimen_on_tuesday,
                      regimen_on_wednesday=regimen_on_wednesday, regimen_on_thursday=regimen_on_thursday,
                      regimen_on_friday=regimen_on_friday, regimen_on_saturday=regimen_on_saturday,
                      regimen_on_sunday=regimen_on_sunday, regimen_time=regimen_time).apply()


async def update_user_email(telegram_id, email):
    user = await User.get(telegram_id)
    await user.update(email=email).apply()


async def update_regimen_on_monday(telegram_id, regimen_on_monday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_monday=regimen_on_monday).apply()


async def update_regimen_on_tuesday(telegram_id, regimen_on_tuesday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_tuesday=regimen_on_tuesday).apply()


async def update_regimen_on_wednesday(telegram_id, regimen_on_wednesday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_wednesday=regimen_on_wednesday).apply()


async def update_regimen_on_thursday(telegram_id, regimen_on_thursday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_thursday=regimen_on_thursday).apply()


async def update_regimen_on_friday(telegram_id, regimen_on_friday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_friday=regimen_on_friday).apply()


async def update_regimen_on_saturday(telegram_id, regimen_on_saturday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_saturday=regimen_on_saturday).apply()


async def update_regimen_on_sunday(telegram_id, regimen_on_sunday):
    user = await User.get(telegram_id)
    await user.update(regimen_on_sunday=regimen_on_sunday).apply()


async def update_time(telegram_id, regimen_time):
    user = await User.get(telegram_id)
    await user.update(regimen_time=regimen_time).apply()
