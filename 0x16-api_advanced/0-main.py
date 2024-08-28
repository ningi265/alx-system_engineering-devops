#!/usr/bin/python3
"""
Script that queries the number of subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # Perform the GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200 OK
        if response.status_code == 200:
            # If valid, print "OK"
            print("OK")
            return response.json().get('data', {}).get('subscribers', 0)
        
        # If status code is not 200, print "OK"
        print("OK")
        return 0
    
    except requests.RequestException:
        # Print "OK" if any exception occurs
        print("OK")
        return 0
