lu-scripting / api_advanced

Python functions that query the [Reddit API](https://www.reddit.com/dev/api/)
without authentication. Every request sets a custom `User-Agent` and does not
follow redirects (invalid subreddits redirect to search results).

## Requirements

- Python 3
- `requests` module (`pip install requests`)
- Code follows PEP8 (`pycodestyle`)

## Files

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the total subscribers, or `0` if the subreddit is invalid. |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` if invalid. |
| `2-recurse.py` | `recurse(subreddit, hot_list=[], after=None)` recursively returns a list of all hot post titles, or `None` if invalid. |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords (case-insensitive, whole words) in hot titles and prints them sorted by count (desc), then alphabetically. |

## Usage

```bash
python3 0-main.py programming
python3 1-main.py programming
python3 2-main.py programming
python3 3-main.py programming 'python java javascript'
```

## Author

sanol-1
