#!/usr/bin/env python3
from sch import codex

TAGS = ["public", "shopping"]


codex.add_search(
    "ebay",
    "https://www.ebay.com/sch/i.html?_nkw=",
    "https://ebay.com",
    "ebay marketplace",
    tags=TAGS,
)
