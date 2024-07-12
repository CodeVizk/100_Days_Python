import requests
import datetime as dt

USER = "codevizk"
TOKEN = "dwyhe7562gfu"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"

graph_config = {
    "id": "g1",
    "name": "Studying graph",
    "unit": "Hrs",
    "type": "int",
    "color": "momiji"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

respon = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(respon.text)


# date = dt.datetime.today()

pixel_endpoint = f"{graph_endpoint}/{graph_config["id"]}"
post_pixel_config = {
    "date": f"20240712",
    "quantity": "2",
}

pixel_res = requests.post(url=pixel_endpoint, json=post_pixel_config, headers=headers)
print(pixel_res.text)