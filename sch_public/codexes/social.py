#!/usr/bin/env python3
from typing import Optional

from sch import codex, query_args

TAGS = ["public", "social"]


@codex.command("reddit", tags=TAGS)
def reddit(subreddit: Optional[str] = None, *args: str) -> str:
    """go to reddit or a subreddit

    if subreddit:
        if args:
            return https://old.reddit.com/r/{subreddit}/search?restrict_sr=on&sort=relevance&t=all&q={*args}
        else:
            return https://old.reddit.com/r/{subreddit}
    else:
        return https://old.reddit.com
    """

    if subreddit:
        if args:
            return f"https://old.reddit.com/r/{subreddit}/search?restrict_sr=on&sort=relevance&t=all&q={query_args(*args)}"
        else:
            return f"https://old.reddit.com/r/{subreddit}"
    else:
        return "https://old.reddit.com"


reddit.add_search(
    "search",
    f"https://old.reddit.com/r/all/search?restrict_sr=on&sort=relevance&t=all&q=",
    f"https://old.reddit.com/r/all",
    "search reddit",
)


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
