#!/usr/bin/python3
"""Module to query Reddit API for subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Python:subreddit.subscriber.counter:v1.0 (by /u/user)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                timeout=10)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers if subscribers else 0
        return 0
    except (requests.RequestException, ValueError, KeyError):
        return 0