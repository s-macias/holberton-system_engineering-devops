#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. """


import json
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts for a subreddit """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    try:
        top = requests.get(
            url, headers=header, allow_redirects=False).json().get('data').get(
            'children')
        for item in range(10):
            print(top[item].get('data').get('title'))
    except:
        print("None")
