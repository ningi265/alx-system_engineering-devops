#!/usr/bin/python3
"""
This module defines a function that queries the Reddit API
to get the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is not found
             or if there is an exception while querying the Reddit API.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subscribers-counter:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

