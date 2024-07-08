import smtplib
import time

import requests
import datetime as dt

MY_LAT = 28.631662
MY_LONG = 77.194120


def is_iss_overhead():
    request = requests.get("http://api.open-notify.org/iss-now.json")
    request.raise_for_status()

    data = request.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    position = (iss_longitude, iss_latitude)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

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

    time = dt.datetime.now().hour
    if time >= sunset or time <= sunrise:
        return True


user = "codevizk@gmail.com"
password = "vydq ennv bbay ydau"
if is_iss_overhead() and is_night():
    time.sleep(60)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=user, password=password)
    connection.sendmail(
        from_addr=user,
        to_addrs="vivek223singh@gmail.com",
        msg="Subject:Look up!\n\nThe ISS is above you in the sky."
    )




