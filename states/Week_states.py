from aiogram.dispatcher.filters.state import StatesGroup, State


class Week(StatesGroup):
    Monday = State()
    Tuesday = State()
    Wednesday = State()
    Thursday = State()
    Friday = State()
    Saturday = State()
    Sunday = State()
    Choice_time = State()


class ChangeDay(StatesGroup):
    ChooseDay = State()
    NewRegimen = State()
    NewTime = State()
