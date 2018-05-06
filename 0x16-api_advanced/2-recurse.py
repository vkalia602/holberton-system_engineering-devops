#!/usr/bin/python3
'''
Module that retrives new hot posts in a subreddit
'''


import requests

def recurse(subreddit, hot_list=[], after=""):
    url = 'http://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    print(url)
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get(url, headers=headers)
    print(response.json())
    print(response.json()['data']['after'])
    if response.status_code != 200 or after is None:
        return (hot_list)
    append_list(response.json(), hot_list)

    return recurse(subreddit, hot_list, after=response.json()['data']['after'])

def append_list(response_dict, hot_list):
    print(response_dict)
    for hot in response_dict['data']['children']:
        hot_list.append(hot['data']['title'])
        print (hot_list)

        return (hot_list)
