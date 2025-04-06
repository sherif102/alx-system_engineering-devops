#!/usr/bin/python3
"""api advanced project"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}.json"
    h = {'User-Agent': 'local'}
    request = requests.get(url, allow_redirects=False, headers=h)
    if request.status_code != 200:
        print("None")
        return
    counter = 0
    body = request.json()["data"]["children"]
    while counter < 10:
        print(body[counter]["data"]["title"])
        counter += 1
