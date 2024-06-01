#!/usr/bin/env python3
from typing import List

from sch import codex, Command, bookmark

TAGS = ["public", "apple"]

apple: Command = codex.add_bookmark(
    "apple", "https://apple.com", "tim apple", tags=TAGS
)


FINANCE_TAGS: List[str] = TAGS + ["finances"]
apple.add_bookmark(
    "card", "https://card.apple.com", "apple card management", tags=FINANCE_TAGS
)


icloud: Command = codex.add_bookmark(
    "icloud", "https://www.icloud.com", "iCloud", tags=TAGS
)

icloud.add_bookmark("settings", "https://www.icloud.com/settings/", "settings")

codex.add_bookmark("mail", "https://www.icloud.com/mail/", "icloud e-mail", tags=TAGS)
