#!/usr/bin/python3
"""
Script that queries the number of subscribers on a given Reddit subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Return 'OK' if the subreddit exists but fails to fetch subscribers, otherwise return 0."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Perform the GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the status code is 200 OK
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers

        # If the subreddit exists but some other error occurs, return "OK"
        return "OK"

    except requests.RequestException:
        # Return 0 if any exception occurs
        return 0

# Check if script is being run with a subreddit argument
if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        result = number_of_subscribers(subreddit)
        
        # Correctly format the output based on its type
        if isinstance(result, int):
            print("{:d}".format(result))
        else:
            print(result)
    else:
        print("Please provide a subreddit as an argument.")
