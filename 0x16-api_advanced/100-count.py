#!/usr/bin/python3
"""
This module defines a function that recursively queries the Reddit API,
parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

import requests
import re
from collections import defaultdict


def count_words(
        subreddit, word_list, hot_list=[], after=None, counts=None
        ):
    """Recursively counts the occurrences of keywords,
      in hot posts for a given subreddit."""
    if counts is None:
        counts = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:keyword-counter:v1.0 (by /u/your_username)"
        }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            # Normalize word_list to lowercase
            normalized_word_list = [word.lower() for word in word_list]

            # Count occurrences of each keyword in the titles
            for post in children:
                title = post['data']['title'].lower()
                for word in normalized_word_list:
                    # Use regex to match whole words only
                    matches = re.findall(
                        r'\b{}\b'.format(re.escape(word)), title
                        )
                    counts[word] += len(matches)

            # Check if there's a next page
            after = data.get('after')
            if after:
                return count_words(
                    subreddit, word_list, hot_list, after, counts
                    )
            else:
                # Sort counts first by descending frequency, 
                # then alphabetically
                sorted_counts = sorted(
                    counts.items(), key=lambda x: (-x[1], x[0])
                    )
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
    