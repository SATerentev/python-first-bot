from Infrastructure import db, weather_api

async def get_weather_for_city(city: str, day_offset=1):
    weather_json = await weather_api.get_weather(city)
    max_temperature = weather_json["daily"]["temperature_2m_max"]
    min_temperature = weather_json["daily"]["temperature_2m_min"]
    if day_offset == 1:
        return f"Сегодня в {city}:\nМаксимальная температура: {max_temperature[0]}\nМинимальная температура: {min_temperature[0]}"
    elif day_offset == 2:
        return f"Завтра в {city}:\nМаксимальная температура: {max_temperature[1]}\nМинимальная температура: {min_temperature[1]}"
    else:
       return "что-то наебнулось"