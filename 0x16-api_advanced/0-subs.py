#!/usr/bin/python3
'''
Module to find subcribers of a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Method that sends get requests to acquire
    data on subscribers on a subreddit
    '''
    url = 'https://api.reddit.com/r'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get('{}/{}/about'.format(url, subreddit),
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
            return(response.json()["data"]["subscribers"])
    else:
        return 0
