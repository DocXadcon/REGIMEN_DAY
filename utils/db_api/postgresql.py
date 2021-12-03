from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        regimen_on_monday varchar(7000) NULL,
        regimen_on_tuesday varchar(7000) NULL,
        regimen_on_wednesday varchar(7000) NULL,
        regimen_on_thursday varchar(7000) NULL,
        regimen_on_friday varchar(7000) NULL, 
        regimen_on_saturday varchar(7000) NULL,
        regimen_on_sunday varchar(7000) NULL,
        regimen_time varchar(255) NULL 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def update_regimen_on_monday(self, regimen_on_monday, telegram_id):
        sql = "UPDATE Users SET regimen_on_monday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_monday, telegram_id, execute=True)

    async def update_regimen_on_tuesday(self, regimen_on_tuesday, telegram_id):
        sql = "UPDATE Users SET regimen_on_tuesday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_tuesday, telegram_id, execute=True)

    async def update_regimen_on_wednesday(self, regimen_on_wednesday, telegram_id):
        sql = "UPDATE Users SET regimen_on_wednesday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_wednesday, telegram_id, execute=True)

    async def update_regimen_on_thursday(self, regimen_on_thursday, telegram_id):
        sql = "UPDATE Users SET regimen_on_thursday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_thursday, telegram_id, execute=True)

    async def update_regimen_on_friday(self, regimen_on_friday, telegram_id):
        sql = "UPDATE Users SET regimen_on_friday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_friday, telegram_id, execute=True)

    async def update_regimen_on_saturday(self, regimen_on_saturday, telegram_id):
        sql = "UPDATE Users SET regimen_on_saturday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_saturday, telegram_id, execute=True)

    async def update_regimen_on_sunday(self, regimen_on_sunday, telegram_id):
        sql = "UPDATE Users SET regimen_on_sunday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_on_sunday, telegram_id, execute=True)

    async def update_time(self, regimen_time, telegram_id):
        sql = "UPDATE Users SET regimen_time=$1 WHERE telegram_id=$2"
        return await self.execute(sql, regimen_time, telegram_id, execute=True)

    async def update_regimen_on_week(self, telegram_id, regimen_on_monday, full_name, username, regimen_on_tuesday,
                                     regimen_on_wednesday, regimen_on_thursday, regimen_on_friday, regimen_on_saturday,
                                     regimen_on_sunday, regimen_time):
        sql = "UPDATE Users SET regimen_on_monday=$2, regimen_on_tuesday=$3, " \
              "regimen_on_wednesday=$4, regimen_on_thursday=$5, regimen_on_friday=$6, regimen_on_saturday=$7, " \
              "regimen_on_sunday=$8, regimen_time=$9, username=$10, full_name=$11 WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, regimen_on_monday, regimen_on_tuesday,
                                  regimen_on_wednesday, regimen_on_thursday, regimen_on_friday, regimen_on_saturday,
                                  regimen_on_sunday, regimen_time, username,full_name, execute=True)

    async def add_user(self, full_name, username, telegram_id, regimen_on_monday, regimen_on_tuesday,
                       regimen_on_wednesday, regimen_on_thursday, regimen_on_friday, regimen_on_saturday,
                       regimen_on_sunday, regimen_time):

        sql = "INSERT INTO Users(full_name, username, telegram_id, regimen_on_monday, " \
              "regimen_on_tuesday, regimen_on_wednesday, regimen_on_thursday, regimen_on_friday, regimen_on_saturday, " \
              "regimen_on_sunday, regimen_time) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11) returning *"

        return await self.execute(sql, full_name, username, telegram_id, regimen_on_monday,
                                  regimen_on_tuesday, regimen_on_wednesday, regimen_on_thursday,
                                  regimen_on_friday, regimen_on_saturday, regimen_on_sunday, regimen_time,
                                  fetchrow=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
