import requests
from decouple import config
BEEKEEPER_RESET_URL = config('BEEKEEPER_RESET_URL')


def reset_ids():
    url = BEEKEEPER_RESET_URL
    response = requests.post(url)
    return response.json()
