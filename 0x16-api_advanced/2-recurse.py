#!/usr/bin/python3
"""
this is a recursive function that query Reddit API
and returns a list of titles or none if invalid
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    this fetches the queries of Reddit API and returns
    titles or none if invalid
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            mt = get_data.get("data")
            title = mt.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
