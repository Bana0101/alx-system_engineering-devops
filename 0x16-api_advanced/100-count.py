#!/usr/bin/python3
"""Module documentation"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """parses the title of all hot articles,
    and prints a sorted count of given keywords"""

    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    info = response.json()

    hot_list = []
    for child in info.get("data").get("children"):
        hot_list.append(child.get("data").get("title"))
    if not hot_list:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_list:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
