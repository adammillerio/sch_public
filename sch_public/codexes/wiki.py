#!/usr/bin/env python3
from sch import codex, query_args

TAGS = ["public", "wiki"]


@codex.command("wiki", tags=TAGS)
def wiki(*args: str) -> str:
    """search or go to wikipedia

    if args:
        return https://en.wikipedia.org/w/index.php?title=Special:Search&search={*args}
    else:
        return https://en.wikipedia.org/wiki/Main_Page
    """

    if args:
        return f"https://en.wikipedia.org/w/index.php?title=Special:Search&search={query_args(*args)}"
    else:
        return "https://en.wikipedia.org/wiki/Main_Page"
