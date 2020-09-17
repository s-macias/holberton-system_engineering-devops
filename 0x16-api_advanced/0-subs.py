#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """


import json
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    try:
        subs = requests.get(
            url, headers=header).json().get("data").get("subscribers")
        return subs
    except:
        return 0
