#!/usr/bin/env python3
from typing import Optional

from urllib.parse import quote_plus

from sch import codex, query_args, bookmark, command, Command, format_doc

TAGS = ["google"]


def google_command(site: str, search_url: str) -> Command:
    if site == "search":
        domain: str = "google.com"
    else:
        domain: str = f"{site}.google.com"

    @command(tags=TAGS)
    @format_doc(site=site, domain=domain, search_url=search_url)
    def google_site(*args: str) -> str:
        """search or go to google {site}

        if args:
            return https://{domain}{search_url}{{*args}}
        else:
            return https://{domain}
        """

        if args:
            return f"https://{domain}{search_url}{query_args(*args)}"
        else:
            return f"https://{domain}"

    return google_site


site_configs = {
    "gdocs": ("docs", "/document/u/0/?q="),
    "gdrive": ("drive", "/drive/u/0/search?q="),
    "g": ("search", "/search?q="),
    "gmail": ("mail", "/mail/u/0/#search/"),
    "gmaps": ("maps", "/maps/search/"),
}

for site, config in site_configs.items():
    codex.add_command(google_command(*config), site)
