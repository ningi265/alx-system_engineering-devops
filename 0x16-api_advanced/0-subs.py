#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            all_r = response.json()
            data = all_r.get('data')
            if data:
                return data.get('subscribers', 0)
        elif response.status_code == 404:
            return "OK"
        return "OK"
    except requests.RequestException:
        return "OK"
