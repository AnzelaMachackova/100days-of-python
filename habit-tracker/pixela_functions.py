from userinfo import USERNAME, TOKEN
from datetime import datetime
import requests

# Pixela endpoints
BASE_URL = "https://pixe.la/v1/users"

# functions for various operations
def create_graph(graph_id, name):
    graph_params = {
        "id": graph_id,
        "name": name,
        "unit": "commit",
        "type": "int",
        "color": "shibafu"
    }
    response = requests.post(f"{BASE_URL}/{USERNAME}/graphs", json=graph_params, headers={"X-USER-TOKEN": TOKEN})
    return response.json()

def update_graph(graph_id, quantity):
    date = datetime.now().strftime("%Y%m%d")
    update_params = {
        "date": date,  # today's date in YYYYMMDD format
        "quantity": str(quantity)
    }
    response = requests.post(f"{BASE_URL}/{USERNAME}/graphs/{graph_id}", json=update_params, headers={"X-USER-TOKEN": TOKEN})
    return response.json()

def get_graph_stats(graph_id):
    response = requests.get(f"{BASE_URL}/{USERNAME}/graphs/{graph_id}/stats", headers={"X-USER-TOKEN": TOKEN})
    return response.json()

def delete_graph(graph_id):
    response = requests.delete(f"{BASE_URL}/{USERNAME}/graphs/{graph_id}", headers={"X-USER-TOKEN": TOKEN})
    return response.json()