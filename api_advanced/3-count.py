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

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json()
        children = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            words = title.split()

            for word in words:
                clean_word = word.rstrip('._!?;,')

                if clean_word in counts:
                    counts[clean_word] += 1

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            filtered = {k: v for k, v in counts.items() if v > 0}
            sorted_counts = sorted(filtered.items(),
                                   key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print("{}: {}".format(word, count))

    except Exception:
        return