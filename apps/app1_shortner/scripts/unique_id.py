# scripts/unique_id.py
import requests
from app1_shortner.models import tbl_UniqueNumberRange
from decouple import config


BEEKEEPER_URL = config('BEEKEEPER_URL')


def get_unique_id():
    # try existing range
    latest_range = tbl_UniqueNumberRange.objects.last()
    if latest_range:
        next_id = latest_range.get_next()
        if next_id:
            return next_id

    # if exhausted, ask Beekeeper
    response = requests.get(BEEKEEPER_URL)
    data = response.json()
    start, end = data["start"], data["end"]

    # save new range
    new_range = tbl_UniqueNumberRange.objects.create(
        start=start, end=end, current=start, server_id=data["server_id"]
    )
    return new_range.current
