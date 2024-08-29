#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {"limit": 10}

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check for valid response status and content type
        if response.status_code != 200:
            print("None")
            return

        # Check if response content is JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            print("None")
            return

        # Parse the JSON response and extract the 'data' section
        results = response.json().get("data")

        # Print the titles of the top 10 hottest posts
        [print(c.get("data").get("title")) for c in results.get("children")]

    except requests.RequestException as e:
        # Handle request exceptions such as connection errors
        print(f"Error fetching data: {e}")
        print("None")
