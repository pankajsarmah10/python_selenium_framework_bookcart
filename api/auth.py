import os

import requests

class Auth:

    @staticmethod
    def login():
        url = os.getenv('URL') + os.getenv('LOGIN')
        login_data = {
            "username": os.getenv('USER_EMAIL'),
            "password": os.getenv('USER_PASSWORD')
        }
        login_headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=login_data, headers=login_headers)
        response_data = response.json()
        return response_data
