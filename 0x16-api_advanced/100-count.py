#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            """Initialize word count dictionary if first call"""
            if not word_count:
                word_count = {word.lower(): 0 for word in word_list}

            """Count occurrences of each word in titles"""
            for post in posts:
                title = post['data']['title'].lower().split()
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += title.count(word_lower)

            """Recursively call the function if there's a next page"""
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                """Sort and print the final counts"""
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.exceptions.RequestException as e:
        return
