#!/usr/bin/env python3
from typing import List

from sch import codex, Command

TAGS = ["public", "games"]


codex.add_search(
    "terraria",
    "https://terraria.fandom.com/wiki/Special:Search?scope=internal&navigationSearch=true&query=",
    "https://terraria.fandom.com/wiki/Terraria_Wiki",
    "terraria wiki",
    tags=TAGS,
    aliases=["t"],
)


ffxiv: Command = codex.add_bookmark(
    "ffxiv",
    "https://na.finalfantasyxiv.com/lodestone/",
    "lodestone (community site)",
    tags=TAGS,
    aliases=["ff"],
)

ffxiv_wiki: Command = ffxiv.add_search(
    "wiki",
    "https://na.finalfantasyxiv.com/lodestone/playguide/db/search/?q=",
    "https://na.finalfantasyxiv.com/lodestone/playguide/db",
    "ffxiv wiki",
)

ffxiv_wiki.add_search(
    "escape",
    "https://ffxiv.gamerescape.com/?&title=Special%3ASearch&search=",
    "https://ffxiv.gamerescape.com/wiki/Main_Page",
    "gamerescape ffxiv wiki",
    tags=TAGS,
)

ffxiv_wiki.add_search(
    "console",
    "https://ffxiv.consolegameswiki.com/mediawiki/index.php?title=Special%3ASearch&go=Go&search=",
    "https://ffxiv.consolegameswiki.com/wiki/FF14_Wiki",
    "consolegames ffxiv wiki",
    tags=TAGS,
)

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


codex.add_search(
    "steam",
    "https://store.steampowered.com/search/?term=",
    "https://store.steampowered.com",
    "game store and client",
    tags=TAGS,
)

backloggery: Command = codex.add_bookmark(
    "backloggery", "https://backloggery.com", "game backlog manager", tags=TAGS
)

glitchwave: Command = codex.add_bookmark(
    "glitchwave", "https://glitchwave.com", "game database", tags=TAGS
)
