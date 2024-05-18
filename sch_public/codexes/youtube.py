#!/usr/bin/env python3
from sch import codex, query_args

TAGS = ["public", "google", "media"]


@codex.command("yt", tags=TAGS)
def youtube(*args: str) -> str:
    """search or go to youtube


    if args:
        return https://youtube.com/results?search_query={*args}
    else:
        return https://youtube.com
    """

    if args:
        return f"https://youtube.com/results?search_query={query_args(*args)}"
    else:
        return "https://youtube.com"


@youtube.command("history")
def youtube_history(*args: str) -> str:
    """search youtube history

    The search query doesn't seem to work even though it does show in the URL.

    if args:
        return https://www.youtube.com/feed/history?query={*args}
    else:
        return https://www.youtube.com/feed/history
    """

    if args:
        return f"https://www.youtube.com/feed/history?query={query_args(*args)}"
    else:
        return "https://www.youtube.com/feed/history"


youtube.add_bookmark(
    "subs", "https://www.youtube.com/feed/subscriptions", "subscriptions"
)
