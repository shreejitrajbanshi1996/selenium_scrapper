import HttpTrigger1.config as config
import requests


def get(url, headers=None):
    if headers == None:
        headers = {
            "Authorization": "Bearer " + config.TOKEN,
            "Content-Type": "application/json"
        }

    return requests.get(url, headers=headers)


def post(url, headers=None, data={}):
    # encoded_url = urllib.parse.quote(url)

    if headers == None:
        headers = {
            "Authorization": "Bearer " + config.TOKEN,
            "Content-Type": "application/json"
        }

    return requests.post(url, headers=headers, data=data)


def patch(url, headers=None, data={}):
    if headers == None:
        headers = {
            "Authorization": "Bearer " + config.TOKEN,
            "Content-Type": "application/json"
        }

    return requests.patch(url, headers=headers, data=data)
