#!/usr/bin/env python
import requests
from region import get_region

def get_weather(area_entry):
    if area_entry == 1:
        return("Not Found! (県は不要)")
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_entry}.json"
    overview_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area_entry}.json"
    forecast_json = requests.get(forecast_url).json()
    overview_json = requests.get(overview_url).json()

    weather_time = forecast_json[0]["timeSeries"][0]["timeDefines"][0]
    weather = forecast_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    overview_time = overview_json["reportDatetime"]
    overview = overview_json["text"]
    weather = weather.replace('　', '')
    overview = overview.replace('　', '')

    return(f"{weather_time}\n{weather}\n\n{overview_time}\n{overview}")

if __name__ == "__main__":
    get_pref = input("Pref > ")
    if get_region(get_pref) == 1:
        print("Region not found! (県は不要)")
    else:
        print(get_weather(get_region(get_pref)))