#!/usr/bin/python3
"""api advanced project"""
import re
import requests


def count_words(subreddit, word_list, counter=0, hot_list=[]):
    if type(subreddit) is not list:
        url = f"https://www.reddit.com/r/{subreddit}.json"
        h = {'User-Agent': 'local'}
        request = requests.get(url, allow_redirects=False, headers=h)

        if request.status_code != 200:
            return
        subreddit = request.json()["data"]["children"]

    hot_list.append(subreddit[counter]["data"]["title"])
    counter += 1

    if counter != len(subreddit):
        return count_words(subreddit, word_list, counter, hot_list)

    new_set = {}
    search_string = " ".join(hot_list)

    for y in word_list.split(' '):
        search = re.findall(y, search_string)
        if search:
            new_set[y] = len(search)
    for key, value in sorted(new_set.items()):
        print(f'{key}: {value}')
