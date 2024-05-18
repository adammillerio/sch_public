#!/usr/bin/env python3
from sch import codex

TAGS = ["apple"]


@codex.command("icloud", tags=TAGS)
def icloud() -> str:
    return "https://www.icloud.com"


@codex.command("mail", tags=TAGS)
def icloud_mail() -> str:
    """icloud e-mail

    iCloud's web UI doesn't have the ability to go to specific searches or folders
    via URL, so this is just a bookmark for now.

    return https://www.icloud.com/mail/
    """

    return "https://www.icloud.com/mail/"


icloud.add_bookmark("settings", "https://www.icloud.com/settings/", "settings")
