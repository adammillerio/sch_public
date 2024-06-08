#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "printing"]


codex.add_search(
    "thingiverse",
    "https://www.thingiverse.com/search?q=",
    "https://www.thingiverse.com",
    "ultimaker thingiverse",
    tags=TAGS,
)
