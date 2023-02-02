import pprint
import requests
from dateutil.parser import parse

WEATHER_API = 'YOUR_YANDEX_API_WEATHER_KEY'
WEATHER_CODRS = {
    "Moscow": {"latitude": 55.833333, "longitude": 37.616667}
}


class YandexWeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"https://api.weather.yandex.ru/v2/forecast?lat={WEATHER_CODRS[city]['latitude']}&lon={WEATHER_CODRS[city]['longitude']}"
        print("Sending HTTP request")
        data = requests.get(url, headers={"X-Yandex-API-Key": WEATHER_API}).json()
        forecast_data = data["forecasts"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["parts"]["day"]["temp_max"]
            })
        self._city_cache[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._wether_forecast = weather_forecast or YandexWeatherForecast()

    def weather_forecast(self):
        return self._wether_forecast.get(self.city)


def _main():
    weather_forecast = YandexWeatherForecast()
    for _ in range(2):
        city_info = CityInfo("Moscow", weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)


if __name__ == "__main__":
    _main()
