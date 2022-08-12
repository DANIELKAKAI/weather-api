import requests
from django.conf import settings
from statistics import median


def temp_calculation(forecast_days):
    daily_max_temps = [day["day"]["maxtemp_c"] for day in forecast_days]
    daily_min_temps = [day["day"]["mintemp_c"] for day in forecast_days]
    maximum = max(daily_max_temps)
    minimum = min(daily_min_temps)
    average = (maximum + minimum) / 2
    median_ = median(daily_min_temps + daily_max_temps)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "median": median_}


def get_temperature(city, days):
    result = None
    endpoint = settings.WEATHER_URL_ENDPOINT
    params = {"key": settings.WEATHER_API_KEY, "q": city}
    if days:
        params["days"] = days
    res = requests.get(endpoint, params=params)
    if res.status_code == 200:
        data = res.json()
        forecast_days = data["forecast"]["forecastday"]
        result = temp_calculation(forecast_days)
    return result
