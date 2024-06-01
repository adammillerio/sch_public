#!/usr/bin/env python3
from sch import codex

TAGS = ["public", "wiki"]


codex.add_search(
    "wiki",
    "https://en.wikipedia.org/w/index.php?title=Special:Search&search=",
    "https://en.wikipedia.org/wiki/Main_Page",
    "wikipedia",
    tags=TAGS,
)
