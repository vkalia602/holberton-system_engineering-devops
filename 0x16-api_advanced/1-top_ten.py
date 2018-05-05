#!/usr/bin/python3
'''
Module that retrieves posts from subreddit using requests package
'''
import requests


def top_ten(subreddit):
    '''
    Method that retrieves 10 hot posts from a subreddit
    '''
    url = 'https://api.reddit.com/r'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get('{}/{}/hot'.format(url, subreddit),
                            headers=headers, allow_redirects=False)
    counter = 0
    titles = []
    if response.status_code == 200:
        for hot in response.json()['data']['children']:
            print(hot['data']['title'])
            counter += 1
            if counter == 10:
                break
    else:
        print('None')
