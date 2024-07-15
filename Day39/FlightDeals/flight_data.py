import requests
from pprint import pprint
import os


SHEET_ENDPOINT = os.environ.get("SHEET_GET")

authorize = {
    "Authorization": os.environ.get("SHEET_GET_KEY")
}


class FlightData:
    def __init__(self):
        self.response = requests.get(url=SHEET_ENDPOINT, headers=authorize)
        pprint(self.response.json())
