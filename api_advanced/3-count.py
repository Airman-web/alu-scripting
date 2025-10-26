#!/usr/bin/python3
"""
Module to recursively query Reddit API and count keyword occurrences
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses titles of all hot articles,
    and prints a sorted count of given keywords.
    
    Args:
        subreddit (str): The name of the subreddit
        word_list (list): List of keywords to count (case-insensitive)
        after (str): The 'after' parameter for pagination
        counts (dict): Dictionary to accumulate word counts
    """
    if counts is None:
        counts = {}
        # Initialize counts for all words in word_list (lowercase)
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] = counts.get(word_lower, 0)
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; API-Practice/1.0)'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code != 200:
            return
        
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')
        
        # Count keywords in titles
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()
            
            for word in words:
                # Remove punctuation from the end
                word_clean = word.strip('._!?;,')
                
                if word_clean in counts:
                    counts[word_clean] += 1
        
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            # Print results
            # Filter out words with zero counts
            filtered_counts = {k: v for k, v in counts.items() if v > 0}
            
            # Sort by count (descending) then alphabetically (ascending)
            sorted_counts = sorted(filtered_counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    
    except Exception:
        return