import requests

MY_LAT = 28.631662
MY_LONG = 77.194120
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "add your own from openweathermap"
parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(endpoint, params=parameter)
response.raise_for_status()
weather = response.json()
# day_weather = response.json()["list"][0]["weather"][0]["id"]
for hour in weather["list"]:
    chk = hour["weather"][0]["id"]
    if chk < 700:
        print("bring an umbrella")
