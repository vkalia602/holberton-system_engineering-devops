#!/usr/bin/python3
'''
Module that retrives new hot posts in a subreddit
'''


import requests


def recurse(subreddit, hot_list=[], after=""):
    '''
    Method that recursively makes API calls using 'after' attribute
    '''
    url = 'http://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200 or after is None:
        return (hot_list)
    append_list(response.json(), hot_list)

    return recurse(subreddit, hot_list, after=response.json()['data']['after'])


def append_list(response_dict, hot_list):
    for hot in response_dict['data']['children']:
        hot_list.append(hot['data']['title'])

    return (hot_list)
