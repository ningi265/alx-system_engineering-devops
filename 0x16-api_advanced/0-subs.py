#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit, or 0 if invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            all_r = response.json()
            data = all_r.get('data')
            if data:
                return data.get('subscribers', 0)
        return 0  # Return 0 if subreddit does not exist or other errors
    except requests.RequestException:
        return 0  # Return 0 if request fails

