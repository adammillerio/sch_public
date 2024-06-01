#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "lab", "network", "dn42", "project"]


dn42: Command = codex.add_search(
    "dn42",
    "https://wiki.dn42.us/search?q=",
    "https://wiki.dn42.us/Home",
    "dn42 simulated internet vpn project",
    tags=TAGS,
)


dn42.add_bookmark(
    "guide", "https://wiki.dn42.us/howto/Getting-Started", "onboarding guide", tags=TAGS
)
