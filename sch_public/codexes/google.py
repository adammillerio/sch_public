#!/usr/bin/env python3
from sch import codex, Command, search

TAGS = ["public", "google"]


def google_command(site: str, search_url: str) -> Command:
    if site == "search":
        domain: str = "google.com"
    else:
        domain: str = f"{site}.google.com"

    return search(
        f"https://{domain}{search_url}",
        f"https://{domain}",
        f"google {site}",
        tags=TAGS,
    )


site_configs = {
    "gdocs": ("docs", "/document/u/0/?q="),
    "gdrive": ("drive", "/drive/u/0/search?q="),
    "g": ("search", "/search?udm=14&q="),
    "gmail": ("mail", "/mail/u/0/#search/"),
    "gmaps": ("maps", "/maps/search/"),
}

for site, config in site_configs.items():
    codex.add_command(google_command(*config), site)


@codex.command("gvoice", tags=TAGS)
def gvoice(*args: str) -> str:
    """google voice

    if args:
        return https://voice.google.com/u/0/search?from=[]&q=[{*args}]
    else:
        return https://voice.google.com
    """

    if args:
        quoted_args = ",".join(f'"{arg}"' for arg in args)

        return f"https://voice.google.com/u/0/search?from=[]&q=[{quoted_args}]"
    else:
        return "https://voice.google.com"
