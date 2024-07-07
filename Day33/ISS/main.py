import requests
import datetime as dt

MY_LAT = 28.631662
MY_LONG = 77.194120


request = requests.get("http://api.open-notify.org/iss-now.json")
request.raise_for_status()

data = request.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
position = (longitude, latitude)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()

sunset = int(data["results"]["sunset"].split("T")[1].split(":"))
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":"))

time = dt.datetime.now()
