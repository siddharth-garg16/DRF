import requests
import json

URL = "http://127.0.0.1/create/"

data = {
    'name':'Siddharth',
    'roll':101,
    'city':'Ratia'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()

print(data)