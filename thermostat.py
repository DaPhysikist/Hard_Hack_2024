import requests
import os
from dotenv import load_dotenv

access_key = ''
load_dotenv(dotenv_path='./homeinfo.env')

url = os.environ.get('URL')

while True:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_key}'
    }

    data1 = {
        "command": "sdm.devices.commands.ThermostatMode.SetMode",
        "params": {
            "mode": "COOL"
        }
    }

    response = requests.post(url, headers=headers, json=data1)
    response_json = response.json()

    if "error" in response_json:
        if response_json["error"]["code"] == 401:
            refresh_url = os.environ.get('REFRESH_URL')
            refresh_response = requests.post(refresh_url)
            refresh_json = refresh_response.json()
            access_key = refresh_json["access_token"]
    else:
        break

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_key}'
}

data2 = {
    "command": "sdm.devices.commands.ThermostatTemperatureSetpoint.SetCool",
    "params": {
        "coolCelsius": 22.0
    }
}

response2 = requests.post(url, headers=headers, json=data2)