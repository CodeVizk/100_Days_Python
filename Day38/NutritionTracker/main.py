import requests
import datetime as dt
import os


EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_id = os.environ["NT_APP_ID"]
api_key = os.environ["NT_API_KEY"]
token = os.environ["SHEET_TOKEN"]
sheet_endpoint = os.environ["SHEET_ENDPOINT"]


GENDER = "male"
WEIGHT_KG = 53
HEIGHT_CM = 172
AGE = 19


header = {
    "x-app-id": app_id,
    "x-app-key": api_key,

}

ex_params = {
    "query": str(input("Which exercise you perform?- ")),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}


response = requests.post(url=EXERCISE_ENDPOINT, json=ex_params, headers=header)
body_data = response.json()
# print(body_data)
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

Authorization = {
     "Authorization": f"Bearer {token}"
}
for exercise in body_data["exercises"]:
    sheets_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    post_session = requests.post(sheet_endpoint, json=sheets_input, headers=Authorization)

    # print(post_session.text)
