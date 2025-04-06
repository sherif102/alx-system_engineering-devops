#!/usr/bin/python3
"""api advanced project"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    h = {'User-Agent': 'local'}
    request = requests.get(url, allow_redirects=False, headers=h)
    return request.json()["data"]["subscribers"]

# print(number_of_subscribers("programming"))
