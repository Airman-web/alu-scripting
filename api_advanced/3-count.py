#!/usr/bin/python3
"""Module to recursively query Reddit API and count keyword occurrences."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively query Reddit API and print sorted count of keywords.

    Args:
        subreddit (str): The name of the subreddit
        word_list (list): List of keywords to count (case-insensitive)
        after (str): The 'after' parameter for pagination
        counts (dict): Dictionary to accumulate word counts
    """
    if counts is None:
        counts = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in counts:
                counts[word_lower] = 0

    if subreddit is None or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Python:subreddit.word.count:v1.0 (by /u/user)'
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)

        if response.status_code != 200:
            if not after:
                return
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()

            for word in words:
                word_clean = word.strip('._!?;,')

                if word_clean in counts:
                    counts[word_clean] += 1

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            filtered_counts = {k: v for k, v in counts.items() if v > 0}

            sorted_counts = sorted(filtered_counts.items(),
                                   key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print("{}: {}".format(word, count))

    except (requests.RequestException, ValueError, KeyError):
        return