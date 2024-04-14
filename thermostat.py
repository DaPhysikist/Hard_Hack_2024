import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./homeinfo.env')
access_key = ""

def get_access_key():
    refresh_url = os.environ.get('REFRESH_URL')
    refresh_response = requests.post(refresh_url)
    refresh_json = refresh_response.json()
    return refresh_json["access_token"]

def post_request(url, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_key}'
    }
    return requests.post(url, headers=headers, json=data)

def trigger_thermostat(temperature):
    global access_key

    url = os.environ.get('URL')
    access_key = get_access_key()

    data1 = {
        "command": "sdm.devices.commands.ThermostatMode.SetMode",
        "params": {
            "mode": "COOL"
        }
    }

    response = post_request(url, data1)
    while response.status_code == 401: 
        access_key = get_access_key()
        response = post_request(url, data1)

    if response.status_code != 200:
        print(f"Failed to set mode: {response.json()}")
        return

    data2 = {
        "command": "sdm.devices.commands.ThermostatTemperatureSetpoint.SetCool",
        "params": {
            "coolCelsius": temperature
        }
    }

    response2 = post_request(url, data2)
    if response2.status_code != 200:
        print(f"Failed to set temperature: {response2.json()}")