import os
import json
import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://www.carousell.com.hk/search/roland%20fp30x"

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

STATE_FILE = "seen.json"


def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )


try:
    with open(STATE_FILE, "r") as f:
        seen = set(json.load(f))
except:
    seen = set()


headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(
    SEARCH_URL,
    headers=headers,
    timeout=30
).text

soup = BeautifulSoup(html, "html.parser")

links = []

for a in soup.find_all("a", href=True):

    href = a["href"]

    if "/p/" in href:

        if href.startswith("/"):
            href = "https://www.carousell.com.hk" + href

        links.append(href)

links = list(dict.fromkeys(links))

new_items = []

for item in links[:20]:

    if item not in seen:
        new_items.append(item)

for item in new_items:

    send_telegram(
        f"新放盤：\n{item}"
    )

seen.update(links[:20])

with open(STATE_FILE, "w") as f:
    json.dump(list(seen), f)
