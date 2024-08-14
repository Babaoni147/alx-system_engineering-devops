Reddit API Query Functions for WordPress
This project contains functions that interact with the Reddit API to fetch information about subreddits. The functions included in this project are designed to query the Reddit API and return various types of data, such as the number of subscribers, the titles of hot posts, and the count of specific keywords in hot articles.

Requirements
Python 3.x
requests library
Installation
To install the required requests library, run:

bash
Copy code
pip install requests
Functions
1. number_of_subscribers(subreddit)
This function queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function returns 0.

Prototype
python
Copy code
def number_of_subscribers(subreddit)
Example Usage
python
Copy code
print(number_of_subscribers('python'))  # Should return the number of subscribers in the 'python' subreddit
print(number_of_subscribers('invalidsubreddit'))  # Should return 0
2. top_ten(subreddit)
This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If the subreddit is invalid, the function prints None.

Prototype
python
Copy code
def top_ten(subreddit)
Example Usage
python
Copy code
top_ten('python')  # Should print the titles of the first 10 hot posts in the 'python' subreddit
top_ten('invalidsubreddit')  # Should print None
3. recurse(subreddit, hot_list=[])
This recursive function queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

Prototype
python
Copy code
def recurse(subreddit, hot_list=[])
Example Usage
python
Copy code
print(recurse('python'))  # Should return a list of titles of all hot articles in the 'python' subreddit
print(recurse('invalidsubreddit'))  # Should return None
4. count_words(subreddit, word_list)
This recursive function queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces). If no posts match or the subreddit is invalid, the function prints nothing.

Prototype
python
Copy code
def count_words(subreddit, word_list)
Example Usage
python
Copy code
count_words('python', ['python', 'java', 'javascript'])  # Should print the count of each keyword in the hot article titles
count_words('invalidsubreddit', ['python', 'java'])  # Should print nothing
Notes
Ensure you set a custom User-Agent to avoid errors related to Too Many Requests.
Invalid subreddits may return a redirect to search results. Make sure your code does not follow these redirects.
