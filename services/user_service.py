from Infrastructure import db

async def try_add_new_user(id: int):
    city = "Москва"
    success = await db.try_add_new_user(id, city)

    if success:
        print(f"ЗАРЕГИСТРИРОВАН НОВЫЙ ЮЗЕР\nUSER_ID = {id}")
    else:
        print("НЕТ НОВЫХ ЮЗЕРОВ")

async def get_city(id: int):
    return await db.get_city(id)

async def change_city(id: int, city: str):
    await db.change_city(id, city)