#!/usr/bin/env python3
from urllib.parse import quote_plus
from typing import Optional

from sch import codex, query_args

TAGS = ["public", "social"]


@codex.command("reddit", tags=TAGS)
def reddit(subreddit: Optional[str] = None) -> str:
    """go to reddit or a subreddit

    if subreddit:
        return https://old.reddit.com/r/{subreddit}
    else:
        return https://old.reddit.com
    """

    if subreddit:
        return f"https://old.reddit.com/r/{subreddit}"
    else:
        return "https://old.reddit.com"


@reddit.command("search", tags=TAGS)
def reddit_search(subreddit: str, *args: str) -> str:
    """search reddit

    return https://old.reddit.com/r/{subreddit}/search?q={*args}&restrict_sr=on&sort=relevance&t=all
    """

    return f"https://old.reddit.com/r/{subreddit}/search?q={query_args(*args)}&restrict_sr=on&sort=relevance&t=all"


@reddit_search.command("all")
def reddit_search_all(*args: str) -> str:
    """search all of reddit

    return https://old.reddit.com/r/all/search?q={*args}&restrict_sr=on&sort=relevance&t=all
    """

    return f"https://old.reddit.com/r/all/search?q={query_args(*args)}&restrict_sr=on&sort=relevance&t=all"


codex.add_bookmark("bsky", "https://bsky.app", "bluesky social", tags=TAGS)
codex.add_bookmark(
    "lobsters", "https://lobste.rs", "lobste.rs link aggregator", tags=TAGS
)
codex.add_bookmark(
    "hn", "https://news.ycombinator.com", "hacker news link aggregator", tags=TAGS
)
codex.add_bookmark("facebook", "https://facebook.com", "zuck's party palace", tags=TAGS)
codex.add_bookmark(
    "messenger", "https://messenger.com", "facebook messenger", tags=TAGS
)
codex.add_bookmark(
    "instagram", "https://instagram.com", "zuck's picture palace", tags=TAGS
)
