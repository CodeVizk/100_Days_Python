import requests

parameter = {
    "amount": 10,
    "type": "boolean"
             }
data = requests.get("https://opentdb.com/api.php", params=parameter)
data.raise_for_status()
questions = data.json()
question_data = questions["results"]

