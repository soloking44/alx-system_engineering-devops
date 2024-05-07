#!/usr/bin/python3
"""Function that display hot posts on Reddit subreddit
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Displays the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    # API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid too many requests errors
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers,
                            params={'limit': '10'}, allow_redirects=False)

    # Check if the request was successfull
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
