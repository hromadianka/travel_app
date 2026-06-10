import requests

BASE_URL = "https://api.artic.edu/api/v1/artworks"


def fetch_artwork(external_id: int):
    url = f"{BASE_URL}/{external_id}"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    data = r.json()
    return data.get("data")