#!/usr/bin/python3
"""
Reddit API Tasks - All Solutions
Complete implementation for tasks 0-3
"""

# ===== TASK 0: 0-subs.py =====
# File: 0-subs.py
"""
Module to query Reddit API for subreddit subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
        
    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; API-Practice/1.0)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0

