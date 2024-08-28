#!/usr/bin/python3
"""
This module defines a function that recursively queries the Reddit API
to return a list of titles for all hot articles in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:recursive-scraper:v1.0 (by /u/your_username)"
        }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            hot_list.extend([child['data']['title'] for child in children])
            
            # Check if there's a next page
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None

