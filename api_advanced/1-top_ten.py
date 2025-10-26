#!/usr/bin/python3
"""Module for querying Reddit API top 10 hot posts."""

import requests


def top_ten(subreddit):
    """
    Print titles of first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:api.advanced:v1.0 (by /u/testuser)'
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)