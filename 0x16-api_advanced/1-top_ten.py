#!/usr/bin/python3
"""  requests module """
import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API
    and returns the number of subscribers """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url)
    if response.status_code >= 300:
        print('None')
    else:
        results = response.json().get("data").get("children")
        [print(child.get("data").get("title")) for child in results]
