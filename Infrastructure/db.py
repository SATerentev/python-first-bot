import aiosqlite
import config

async def try_add_new_user(user_id: int, user_city: str):
    success = False
    async with aiosqlite.connect(config.DB) as db:
        async with db.execute("SELECT 1 FROM Users WHERE id = ?", (user_id, )) as cursor:
            if await cursor.fetchone() is None:
                await db.execute(
                    "INSERT INTO Users VALUES (?, ?)", (user_id, user_city)
                )
                success = True
        await db.commit()
        return success


async def get_city(user_id: int):
    async with aiosqlite.connect(config.DB) as db:
        cursor = await db.execute("SELECT city FROM Users WHERE id = ?", (user_id, ))
        row = await cursor.fetchone()
        city = row[0]
        return city