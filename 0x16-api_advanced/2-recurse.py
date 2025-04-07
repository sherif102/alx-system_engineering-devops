#!/usr/bin/python3
"""api advanced project"""
import requests


def recurse(subreddit, hot_list=[], counter=0):
    if type(subreddit) != list:
        url = f"https://www.reddit.com/r/{subreddit}.json"
        h = {'User-Agent': 'local'}
        request = requests.get(url, allow_redirects=False, headers=h)

        if request.status_code != 200:
            return "not 200"
        subreddit = request.json()["data"]["children"]

    hot_list.append(subreddit[counter]["data"]["title"])
    counter += 1

    if counter != len(subreddit):
        return recurse(subreddit, hot_list, counter)
    return hot_list

print(recurse("programming"))