#!/usr/bin/env python3
from typing import List

from sch import codex, query_args

TAGS = ["books"]


# TODO: (*) should be added to all commands which take *args as an alternative
# to writing "search or go to" in the help for it.
@codex.command("librarything", tags=TAGS)
def librarything(*args: str) -> str:
    """book aggregator

    if args:
        return https://www.librarything.com/search.php?searchtype=newwork_titles&sortchoice=0&search={*args}
    else:
        return https://www.librarything.com
    """

    if args:
        return f"https://www.librarything.com/search.php?searchtype=newwork_titles&sortchoice=0&search={query_args(*args)}"
    else:
        return "https://www.librarything.com"


codex.add_bookmark(
    "bookworm", "https://www.bookwormreads.co/home", "book aggregator", tags=TAGS
)


AMZN_TAGS: List[str] = TAGS + ["amazon"]


@codex.command("goodreads", tags=AMZN_TAGS)
def goodreads(*args: str) -> str:
    """book aggregator

    if args:
        return https://www.goodreads.com/search?q={*args}
    else:
        return https://www.goodreads.com
    """

    if args:
        return f"https://www.goodreads.com/search?q={query_args(*args)}"
    else:
        return "https://www.goodreads.com"
