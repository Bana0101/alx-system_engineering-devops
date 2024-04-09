#!/usr/bin/python3
"""  requests module """
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API
    and returns the number of subscribers """
    try:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={"User-Agent": "checker by yourusername"},
            allow_redirects=False)
        if response.status_code == 200:
            response = response.json()
            return response['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except Exception as e:
        return 0
