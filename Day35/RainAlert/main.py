import requests
import smtplib

USER = "YOUR EMAIL @gmail.com"
PASS = "YOUR PASSWORD"
MY_LAT = 28.631662
MY_LONG = 77.194120
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR KEY"
parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(endpoint, params=parameter)
response.raise_for_status()
weather = response.json()
will_rain = False
for hour in weather["list"]:
    condition = hour["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    connect = smtplib.SMTP("smtp.gmail.com")
    connect.starttls()
    connect.login(user=USER, password=PASS)
    connect.sendmail(from_addr=USER, to_addrs="RECEIVER EMAIL", msg="Subject: Weather update\n\nIt's going to rain "
                                                                        "today get an umbrella")
    connect.close()
