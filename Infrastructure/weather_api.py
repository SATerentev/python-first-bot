import config, aiohttp

async def get_weather(city: str):
    lat = config.CITIES[city]["lat"]
    lon = config.CITIES[city]["lon"]

    async with aiohttp.ClientSession() as session:
        async with session.get(config.API_URL(lat, lon)) as response:
            if response.status == 200:
                weather_data = await response.json()
                print(weather_data)
                return weather_data
            else:
                return "Ошибка openweather"
