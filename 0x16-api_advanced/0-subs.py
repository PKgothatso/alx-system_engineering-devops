#!/usr/bin/python3
"""Script that queries the number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set a custom User-Agent to identify your application
    user_agent = {"User-Agent": "Google Chrome Version 125.0.6422.142"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Use requests.get with allow_redirects=False
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        try:
            results = response.json()
            return results.get("data", {}).get("subscribers", 0)
        except Exception:
            return 0
    else:
        return 0
