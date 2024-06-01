#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "obsidian", "docs"]


obsidian: Command = codex.add_bookmark(
    "obsidian", "https://help.obsidian.md/Home", "obsidian note taking app", tags=TAGS
)

obsidian.add_bookmark(
    "uri",
    "https://help.obsidian.md/Extending+Obsidian/Obsidian+URI",
    "obsidian uri reference",
    tags=TAGS,
)
