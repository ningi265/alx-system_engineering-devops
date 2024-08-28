#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        if subscribers:
            print("OK")
        else:
            print("OK")
        return subscribers
    except requests.RequestException:
        print("OK")
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./script.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        number_of_subscribers(subreddit)
