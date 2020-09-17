# 0x16. API advanced

## Learning Objectives
How to read API documentation to find the endpoints you’re looking for
How to use an API with pagination
How to parse JSON results from an API
How to make a recursive API call
How to sort a dictionary by value

## Tasks

### 0. How many subs? mandatory

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
File: 0-subs.py

### 1. Top Ten mandatory

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
File: 1-top_ten.py

### 2. Recurse it! mandatory

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
File: 2-recurse.py

### 3. Count it! #advanced

Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
File: 100-count.py
