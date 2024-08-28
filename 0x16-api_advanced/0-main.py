#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = number_of_subscribers(sys.argv[1])
        
        # Check if the result is an integer and format accordingly
        if isinstance(result, int):
            print("{:d}".format(result))
        else:
            print(result)
