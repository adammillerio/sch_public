#!/usr/bin/env python3
from typing import List
from urllib.parse import quote_plus

from sch import codex

TAGS = ["games"]


@codex.command("t", tags=TAGS)
def terraria(*args: str) -> str:
    """search or go to terraria wiki

    if args:
        return https://terraria.fandom.com/wiki/Special:Search?scope=internal&navigationSearch=true&query={query}
    else:
        return https://terraria.fandom.com/wiki/Terraria_Wiki
    """

    if args:
        query = quote_plus(" ".join(args))

        return f"https://terraria.fandom.com/wiki/Special:Search?scope=internal&navigationSearch=true&query={query}"
    else:
        return "https://terraria.fandom.com/wiki/Terraria_Wiki"


terraria.add_bookmark("wiki", "https://terraria.fandom.com/wiki/Terraria_Wiki", "wiki")


@codex.command("ff", tags=TAGS)
def ffxiv() -> str:
    """lodestone (community site)

    return https://na.finalfantasyxiv.com/lodestone/
    """

    return "https://na.finalfantasyxiv.com/lodestone/"


@ffxiv.command("wiki")
def ffxiv_wiki(*args: str) -> str:
    """search or go to FFXIV wiki

    if args:
        return https://na.finalfantasyxiv.com/lodestone/playguide/db/search/?q={*args}
    else:
        return https://na.finalfantasyxiv.com/lodestone/playguide/db
    """

    if args:
        query = quote_plus(" ".join(args))

        return (
            f"https://na.finalfantasyxiv.com/lodestone/playguide/db/search/?q={query}"
        )
    else:
        return "https://na.finalfantasyxiv.com/lodestone/playguide/db"


@ffxiv_wiki.command("escape")
def ffxiv_wiki_gamerescape(*args: str) -> str:
    """gamerescape ffxiv wiki

    if args:
        return https://ffxiv.gamerescape.com/?&title=Special%3ASearch&search={*args}
    else:
        return https://ffxiv.gamerescape.com/wiki/Main_Page
    """

    if args:
        query = quote_plus(" ".join(args))

        return f"https://ffxiv.gamerescape.com/?&title=Special%3ASearch&search={query}"
    else:
        return "https://ffxiv.gamerescape.com/wiki/Main_Page"


@ffxiv_wiki.command("console")
def ffxiv_wiki_consolegameswiki(*args: str) -> str:
    """consolegames ffxiv wiki

    if args:
        return https://ffxiv.consolegameswiki.com/mediawiki/index.php?title=Special%3ASearch&go=Go&search={*args}
    else:
        return https://ffxiv.consolegameswiki.com/wiki/FF14_Wiki
    """

    if args:
        query = quote_plus(" ".join(args))

        return f"https://ffxiv.consolegameswiki.com/mediawiki/index.php?title=Special%3ASearch&go=Go&search={query}"
    else:
        return "https://ffxiv.consolegameswiki.com/wiki/FF14_Wiki"


ffxiv.add_bookmark("data", "https://www.garlandtools.org/db/", "garland data db")

ffxiv.add_bookmark(
    "mogstation",
    "https://secure.square-enix.com/account/app/svc/ffxivshopacctop",
    "account management",
)

BLOG_TAGS: List[str] = TAGS + ["blogs"]

codex.add_bookmark(
    "kimimi",
    "https://kimimithegameeatingshemonster.com",
    "the game eating she-monster",
    tags=BLOG_TAGS,
)
