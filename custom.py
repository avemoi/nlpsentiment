import requests
from requests.structures import CaseInsensitiveDict

import settings

HEADERS = CaseInsensitiveDict()
HEADERS["Accept"] = "application/json"
HEADERS["Authorization"] = f"Bearer {settings.BEARER}"


def search_tweets(query, max_pages, current_page=None, twlist=None, next=None):
    if twlist is None:
        twlist = []
        current_page = 0

    current_page += 1
    resp = requests.get(
        settings.API_URL, params={"query": query, "next_token": next}, headers=HEADERS
    )
    resp_json = resp.json()
    data = resp_json.get("data", [])
    twlist += [obj for obj in data]
    next = resp.json().get("meta", {}).get("next_token", None)

    if current_page == max_pages:
        return twlist

    if next:
        return search_tweets(query, max_pages, current_page, twlist, next=next)

    return twlist
