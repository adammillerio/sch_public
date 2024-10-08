#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "music", "social"]


rym: Command = codex.add_search(
    "rym",
    "https://rateyourmusic.com/search?searchtype=&searchterm=",
    "https://rateyourmusic.com",
    "rate your music",
    tags=TAGS,
)


lastfm: Command = codex.add_search(
    "lastfm",
    "https://last.fm/search?q=",
    "https://last.fm",
    "last.fm listening tracker",
    tags=TAGS,
)


music: Command = codex.add_bookmark(
    "music", "https://www.youtube.com/watch?v=Q5jZXE3bNPg", "it's music", tags=TAGS
)


deezer: Command = codex.add_search(
    "deezer",
    "https://www.deezer.com/search/",
    "https://www.deezer.com/us/channels/explore",
    "hi-fi music streaming catalog",
    escaped=True,
    tags=TAGS,
)

bandcamp: Command = codex.add_search(
    "bandcamp",
    "https://bandcamp.com/search?item_type=&q=",
    "https://bandcamp.com",
    "indie music store",
    tags=TAGS,
    aliases=["bc"],
)

bandcamp.add_bookmark(
    "friday", "https://isitbandcampfriday.com", "is it bandcamp friday?"
)

codex.add_search(
    "musicbrainz",
    "https://musicbrainz.org/search?type=artist&method=indexed&query=",
    "https://musicbrainz.org",
    "music db",
    tags=TAGS,
    aliases=["brainz"],
)
