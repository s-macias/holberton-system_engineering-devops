#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. Done recursively """


import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Prints the titles of the first 10 hot posts for a subreddit """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10?after={}".format(
            subreddit, after)
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    url_req = requests.get(
        url, headers=header, allow_redirects=False).json().get('data')
    top = url_req.get('children')
    if top is None:
        return None
    else:
        after = url_req.get('after')
        for post in top:
            hot_list.append(post.get('data').get('title'))
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
