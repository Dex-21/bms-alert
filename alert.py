import os, requests

URL = os.environ["BMS_URL"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
HEADERS = {"User-Agent": "Mozilla/5.0"}

def notify(msg):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

r = requests.get(URL, headers=HEADERS, timeout=20)
print("status:", r.status_code)
if r.status_code == 200 and "Book tickets" in r.text:  # tweak this check
    notify(f"Bookings may be open! {URL}")
