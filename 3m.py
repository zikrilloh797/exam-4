import threading
import time
from datetime import timedelta
import httpx
import redis


def get_website_data(url):
    response = httpx.get(url).read()
    response.decode('utf-8')
    con = redis.Redis(host="localhost", port=6379, decode_responses=True)
    con.set(name=url, value=response, ex=timedelta(60))


websites = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.kun.uz",
    "https://www.github.com",
    "https://www.daryo.uz"
]

threads = []
for website in websites:
    start = time.time()
    thread = threading.Thread(target=get_website_data, args=(website,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
