from typing import Union

import asyncpg
from asyncpg import Pool, Connection

from data import settings


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=settings.DB_USER,
            password=settings.DB_PASS,
            host=settings.DB_HOST,
            database=settings.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch=False,  # забираем все данные базы данных
                      fetchrow=False,  # забираем одну запись (строку) в базе данных
                      fetchval=False,  # забираем одно значение
                      execute=False):
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
        CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        status_deleted BOOLEAN NOT NULL DEFAULT FALSE,
        invited_users INT NOT NULL DEFAULT 0,
        is_invited  BOOLEAN NOT NULL DEFAULT FALSE,
        generated_passwords INT NOT NULL DEFAULT 0,
        chosen_types varchar(255) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, username, telegram_id):
        sql = "INSERT INTO users(username, telegram_id) VALUES($1, $2) RETURNING *"
        return await self.execute(sql, username, telegram_id, execute=True, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetch=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def get_telegram_id(self):
        sql = "SELECT telegram_id FROM users WHERE status_deleted=false"
        return await self.execute(sql, fetch=True)

    async def count_all_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def count_deleted_users(self):
        sql = "SELECT COUNT(*) FROM Users WHERE status_deleted=true"
        return await self.execute(sql, fetchval=True)

    async def count_invited_users(self):
        sql = "SELECT COUNT(*) FROM Users WHERE is_invited=true"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE True", execute=True)

    async def delete_user(self, telegram_id):
        await self.execute("DELETE FROM Users WHERE telegram_id=$1", telegram_id, execute=True)

    async def drop_table_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def status_deleted_true(self, telegram_id):
        sql = "UPDATE Users SET status_deleted=true WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def status_deleted_false(self, telegram_id):
        sql = "UPDATE Users SET status_deleted=false WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def update_invited_users(self, inveted_users, telegram_id):
        sql = "UPDATE Users SET invited_users=$1 WHERE telegram_id=$2"
        await self.execute(sql, inveted_users, telegram_id, execute=True)

    async def is_invited(self, telegram_id):
        sql = "UPDATE Users SET is_invited=true WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def change_pass_type(self, telegram_id, chosen_types):
        sql = "UPDATE Users SET chosen_types=$2 WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, chosen_types, execute=True)

    async def get_generated_passwords(self):
        sql = "SELECT generated_passwords FROM users WHERE TRUE"
        return await self.execute(sql, fetch=True)

    async def update_generated_passwords(self, telegram_id, generated_password):
        sql = "UPDATE Users SET generated_passwords=$2 WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, generated_password, execute=True)
