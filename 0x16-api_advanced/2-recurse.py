#!/usr/bin/python3
"""Module for task 2"""
    import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """returns a list containing the titles of all
    hot articles for a given subreddit"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    for child in response.json().get("data").get("children"):
        hot_list.append(child.get("data").get("title"))

    info = response.json()
    if not info.get("data").get("after"):
        return hot_list

    return recurse(subreddit, hot_list, info.get("data").get("count"),
                   info.get("data").get("after"))
