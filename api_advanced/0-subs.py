#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a subreddit.

    Return 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/sanol-1)"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
