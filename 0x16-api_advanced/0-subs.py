#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0


def test_existing_subreddit(subreddit):
    """Test function with an existing subreddit."""
    subscribers = number_of_subscribers(subreddit)
    if subscribers > 0:
        print(f"Number of subscribers in r/{subreddit}: {subscribers}")
    else:
        print(f"Subreddit r/{subreddit} does not exist or has no subscribers.")


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    test_existing_subreddit(subreddit)
