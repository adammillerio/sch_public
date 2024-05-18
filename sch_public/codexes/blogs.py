#!/usr/bin/env python3
from typing import Iterable

from sch import codex, query_args, command, Command, format_doc

TAGS = ["public", "blogs", "writing"]


def blog_command(
    url: str, search_url: str, short_help: str, tags: Iterable[str]
) -> Command:
    tags = set(tags)
    tags.add("blogs")
    tags.add("public")

    @command(tags=tags)
    @format_doc(short_help=short_help, url=url, search_url=search_url)
    def blog_site(*args: str) -> str:
        """{short_help}

        if args:
            return {search_url}{{*args}}
        else:
            return {url}
        """

        if args:
            return f"{search_url}{query_args(*args)}"
        else:
            return url

    return blog_site


blogs = {
    "aftermath": (
        "https://aftermath.site",
        "https://aftermath.site/search?s=",
        "gaming blog",
        ["games"],
    ),
    "hellgate": (
        "https://hellgatenyc.com",
        "https://hellgatenyc.com/search?s=",
        "nyc news blog",
        ["nyc"],
    ),
    "404": (
        "https://www.404media.co/",
        # No URL based search, so this is more or less just a google "proxy"
        "https://www.google.com/search?q=404media+",
        "tech blog",
        ["tech"],
    ),
    "express": (
        "https://nicole.express/",
        # No URL based search, so this is more or less just a google "proxy"
        "https://www.google.com/search?q=nicole+express+",
        "retro games blog",
        ["tech", "retro", "games", "hardware"],
    ),
    "whatskenmaking": (
        "https://whatskenmaking.com/articles/",
        "https://whatskenmaking.com/?s=",
        "retro emulation and tech blog",
        ["tech", "retro", "games", "hardware"],
    ),
}

for name, config in blogs.items():
    codex.add_command(blog_command(*config), name)
