from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def find_user(user_id: str):
    url = f"https://vk.com/id{user_id}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, "html.parser")
    status = soup.find("div", {"class", "profile_online_lv"})

    if status != "Online":
        status = "Ofline"

    return status
