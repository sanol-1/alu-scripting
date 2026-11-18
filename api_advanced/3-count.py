#!/usr/bin/python3
"""Module that recursively counts keywords in the hot post titles."""
import requests


def print_counts(counts, word_list):
    """Print keyword counts sorted by count (desc) then name (asc)."""
    repeats = {}
    for word in word_list:
        repeats[word.lower()] = repeats.get(word.lower(), 0) + 1
    totals = {w: counts.get(w, 0) * n for w, n in repeats.items()}
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        if total > 0:
            print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Print nothing if the subreddit is invalid or no keyword matches.
    """
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/sanol-1)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return print_counts(counts, word_list)
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return print_counts(counts, word_list)

    targets = set(w.lower() for w in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in targets:
                counts[token] = counts.get(token, 0) + 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)
    return print_counts(counts, word_list)
