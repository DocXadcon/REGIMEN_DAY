from sqlalchemy.orm.identity import IdentityMap
from sqlalchemy.util import IdentitySet

from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Integer, Column, BigInteger, String, sql, Computed, INTEGER, Interval, ForeignKey
from sqlalchemy.schema import Sequence


class User(TimedBaseModel):
    __tablename__ = "users"
    telegram_id = Column(BigInteger, primary_key=True)
    id = Column(Integer, Sequence("start=1"))
    name = Column(String(100))
    email = Column(String(100))
    regimen_on_monday = Column(String(7999))
    regimen_on_tuesday = Column(String(7999))
    regimen_on_wednesday = Column(String(7999))
    regimen_on_thursday = Column(String(7999))
    regimen_on_friday = Column(String(7999))
    regimen_on_saturday = Column(String(7999))
    regimen_on_sunday = Column(String(7999))
    regimen_time = Column(BigInteger)

    referral = Column(BigInteger)

    def __repr__(self):
        # return {"id": {self.id}, "name": {self.name}, "email": {self.email}}
        return f'{self.id} {self.telegram_id} {self.name} {self.email} {self.regimen_on_monday} {self.regimen_on_tuesday}' \
               f'{self.regimen_on_wednesday} {self.regimen_on_thursday} {self.regimen_on_friday}' \
               f'{self.regimen_on_saturday} {self.regimen_on_sunday} {self.regimen_time}'

    query: sql.Select
