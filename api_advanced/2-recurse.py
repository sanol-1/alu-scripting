#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of the titles of all hot posts of a subreddit.

    Return None if the subreddit is invalid or has no results.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/sanol-1)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return hot_list if hot_list else None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list if hot_list else None

    titles = [p.get("data", {}).get("title") for p in data.get("children", [])]
    hot_list = hot_list + titles
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
