#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print titles of first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Python:subreddit.top.posts:v1.0 (by /u/user)'
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            print(None)
    except (requests.RequestException, ValueError, KeyError):
        print(None)