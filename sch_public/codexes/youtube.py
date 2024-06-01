#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "google", "media"]


youtube: Command = codex.add_search(
    "youtube",
    "https://youtube.com/results?search_query=",
    "https://youtube.com",
    "youtube",
    tags=TAGS,
    aliases=["yt"],
)


youtube.add_search(
    "history",
    "https://www.youtube.com/feed/history?query=",
    "https://www.youtube.com/feed/history",
    "watch history",
    tags=TAGS,
)

youtube.add_bookmark(
    "subs", "https://www.youtube.com/feed/subscriptions", "subscriptions"
)
