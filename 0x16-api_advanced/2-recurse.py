#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all hot article titles for a given subreddit."""
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    hot_list.extend([child['data']['title'] for child in data['children']])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
