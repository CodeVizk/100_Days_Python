import requests
import datetime as dt


PIXELA_ENDPOINT = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# Creating a user in Pixela
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)


# Creating a header for header request
headers = {
    "X-USER-TOKEN": TOKEN
}


# Creating a Graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
graph_config = {
    "id": "g1",
    "name": "Studying graph",
    "unit": "Hrs",
    "type": "int",
    "color": "momiji"
}

respon = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# Adding data to graph
date = dt.datetime.today().strftime("%Y%m%d")
pixel_endpoint = f"{graph_endpoint}/{graph_config["id"]}"

post_pixel_config = {
    "date": date,
    "quantity": input(int("How many hours did you study")),
}


pixel_res = requests.post(url=pixel_endpoint, json=post_pixel_config, headers=headers)


# Updating pixel
# update_pixel_endpoint = f"{pixel_endpoint}/{date}"
# update_pixel_config = {
#     "quantity": "1"
# }


# Deleting pixel
# update_pixel = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# delete_pixel = requests.delete(url=update_pixel_endpoint,headers=headers)
# print(delete_pixel.text)