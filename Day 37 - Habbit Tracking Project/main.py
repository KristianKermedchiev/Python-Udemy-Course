import requests
from datetime import datetime

TOKEN = "<token>"
USERNAME = "<username>"
GRAPH_ID = "<graphId>"
today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

headers = {
        "X-USER-TOKEN": TOKEN
}


def create_user(token, username):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    return requests.post(url=pixela_endpoint, json=user_params)


def create_graph():
    graph_config = {
        "id": "graph1",
        "name": "My Graph",
        "unit": "rep",
        "type": "int",
        "color": "sora"
    }

    return requests.post(url=graph_endpoint, json=graph_config, headers=headers)


def update_pixel(quantity):

    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity,
    }

    return requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)


def change_pixel(quantity, date):

    new_pixel_data = {
        "date": date.strftime('%Y%m%d'),
        "quantity": quantity,
    }

    return requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


def delete_pixel(date):

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

    return requests.delete(url=delete_endpoint, headers=headers)