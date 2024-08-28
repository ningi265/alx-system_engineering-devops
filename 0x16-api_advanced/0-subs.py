#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {'User-Agent': 'my-custom-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            all_r = response.json()
            data = all_r.get('data', {})
            sub_count = data.get('subscribers', 0)
            return sub_count
        else:
            return 0
    except requests.RequestException as error:
        print(f"An error occurred: {error}")
        return 0

