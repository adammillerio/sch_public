#!/usr/bin/env python3
from typing import Iterable

from sch import codex, search, Command

TAGS = ["public", "blogs", "writing"]


def blog_command(
    url: str, search_url: str, short_help: str, tags: Iterable[str]
) -> Command:
    tags = set(tags)
    tags.add("blogs")
    tags.add("public")
    tags.add("writing")

    return search(search_url, url, short_help, tags=tags)


blogs = {
    "aftermath": (
        "https://aftermath.site",
        "https://aftermath.site/search?s=",
        "gaming blog",
        ["games", "subscription"],
    ),
    "hellgate": (
        "https://hellgatenyc.com",
        "https://hellgatenyc.com/search?s=",
        "nyc news blog",
        ["nyc", "subscription"],
    ),
    "404": (
        "https://www.404media.co/",
        # No URL based search, so this is more or less just a google "proxy"
        "https://www.google.com/search?q=site:404media.co+",
        "tech blog",
        ["tech"],
    ),
    "express": (
        "https://nicole.express/",
        # No URL based search, so this is more or less just a google "proxy"
        "https://www.google.com/search?q=site:nicole.express+",
        "retro games blog",
        ["tech", "retro", "games", "hardware"],
    ),
    "whatskenmaking": (
        "https://whatskenmaking.com/articles/",
        "https://whatskenmaking.com/?s=",
        "retro emulation and tech blog",
        ["tech", "retro", "games", "hardware"],
    ),
    "pagedout": (
        "https://pagedout.institute/?page=issues.php",
        "https://www.google.com/search?q=site:pagedout.institute+",
        "one-pager programming articles",
        ["tech", "code"],
    ),
    "hydra": (
        "https://flaminghydra.com",
        "https://www.google.com/search?q=site:flaminghydra.com+",
        "daily newsletter",
        ["subscription"],
    ),
    "leadedsolder": (
        "https://www.leadedsolder.com",
        "https://www.google.com/search?q=site:leadedsolder.com+",
        "retro computer restoration",
        ["tech"],
    ),
    "dtdb": (
        "https://www.downtowndougbrown.com",
        "https://www.google.com/search?q=site:downtowndougbrown.com+",
        "linux/embedded projects",
        ["tech"],
    ),
}

for name, config in blogs.items():
    codex.add_command(blog_command(*config), name)
