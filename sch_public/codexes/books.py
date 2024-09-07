#!/usr/bin/env python3
from typing import List

from sch import codex

TAGS = ["public", "books"]


codex.add_search(
    "librarything",
    "https://www.librarything.com/search.php?searchtype=newwork_titles&sortchoice=0&search=",
    "https://www.librarything.com",
    "book aggregator",
    tags=TAGS,
)


codex.add_bookmark(
    "bookworm", "https://www.bookwormreads.co/home", "book aggregator", tags=TAGS
)


AMZN_TAGS: List[str] = TAGS + ["amazon"]


codex.add_search(
    "goodreads",
    "https://www.goodreads.com/search?q=",
    "https://www.goodreads.com",
    "book aggregator",
    tags=AMZN_TAGS,
)


codex.add_search(
    "libro",
    "https://libro.fm/search?utf8=✓&q=",
    "https://libro.fm",
    "audiobook store",
    tags=TAGS,
)
