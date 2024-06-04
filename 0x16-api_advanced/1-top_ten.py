#!/usr/bin/python3
"""Script to print the first 10 hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        None: If an error occurs or the subreddit is invalid.
    """

    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Send a GET request to the subreddit's hot posts page
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for successful response (status code 200)
        if response.status_code == 200:
            try:
                results = response.json()
                children = results.get("data", {}).get("children", [])
                [print(child.get("data", {}).get("title")) for child
                 in children[:10]]
            except JSONDecodeError as e:
                print(f"Error: Failed to decode JSON response. ({e})")
                return None
        else:
            # Handle non-200 status codes (e.g., 404 Not Found)
            print("None")
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed. ({e})")
        return None

    return None
