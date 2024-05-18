#!/usr/bin/env python3
from sch import codex, query_args, escape_args

TAGS = ["music", "social"]


@codex.command("rym", tags=TAGS)
def rym(*args: str) -> str:
    """search or go to rate your music aggregator

    if args:
        return https://rateyourmusic.com/search?searchtype=&searchterm={*args}
    else:
        return https://rateyourmusic.com
    """

    if args:
        return f"https://rateyourmusic.com/search?searchtype=&searchterm={query_args(*args)}"
    else:
        return "https://rateyourmusic.com"


@codex.command("lastfm", tags=TAGS)
def lastfm(*args: str) -> str:
    """search or go to last.fm listening tracker

    if args:
        return https://www.last.fm/search?q={*args}
    else:
        return https://last.fm
    """

    if args:
        return f"https://last.fm/search?q={query_args(*args)}"
    else:
        return "https://last.fm"


@codex.command("music", tags=TAGS)
def music() -> str:
    """it's music"""

    return "https://www.youtube.com/watch?v=Q5jZXE3bNPg"


@codex.command("deezer", tags=TAGS)
def deezer(*args: str) -> str:
    """hi-fi music streaming catalog

    if args:
        return https://www.deezer.com/search/*args
    else:
        return https://www.deezer.com/us/channels/explore
    """

    if args:
        return f"https://www.deezer.com/search/{escape_args(*args)}"
    else:
        return "https://www.deezer.com/us/channels/explore"
