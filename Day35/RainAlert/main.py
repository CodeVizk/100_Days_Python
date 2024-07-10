import requests

MY_LAT = 28.631662
MY_LONG = 77.194120
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f500d64e87b7c125b5eae2a366a49cfd"
parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}


request = requests.get(endpoint, params=parameter)
request.raise_for_status()

print(request.json())
