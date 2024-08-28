#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:sub.count:v1.0 (by /u/yourusername)'}

    try:
        # Make the request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if response status is OK
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
