#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot articles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query Reddit API and return list of all hot post titles.

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): List to accumulate hot post titles
        after (str): The 'after' parameter for pagination

    Returns:
        list: List of all hot post titles, or None if invalid subreddit
    """
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Python:subreddit.hot.recurse:v1.0 (by /u/user)'
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    hot_list.append(title)

            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        return None
    except (requests.RequestException, ValueError, KeyError):
        return None