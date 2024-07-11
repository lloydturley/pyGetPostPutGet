import os

import requests
from datetime import datetime

# https://pixe.la/v1/users/larrytearly/graphs/stepsgraph.html

USERNAME = os.environ['PIXELA_USERNAME']
TOKEN = os.environ['PIXELA_TOKEN']
GRAPHID = os.environ['PIXELA_GRAPHID']

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name":"Steps Graph",
    "unit": "Steps",
    "type":"int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

# today = datetime.now()

yesterday = datetime(month=7, day=10, year=2024)
today = datetime.now()

add_data = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "10000"
}

# response = requests.post(url=add_endpoint, json=add_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterday.strftime("%Y%m%d")}"

update_data = {
    "quantity" : "1000"
}
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# delete
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)