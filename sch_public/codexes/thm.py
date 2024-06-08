#!/usr/bin/env python3
from sch import codex, Command

# https://github.com/danielmiessler/SecLists/tree/master

TAGS = ["public", "security"]


codex.add_bookmark("thm", "https://tryhackme.com", "TryHackMe", tags=TAGS)

hacktricks: Command = codex.add_search(
    "hacktricks",
    "https://book.hacktricks.xyz/?q=",
    "https://book.hacktricks.xyz",
    "hacktricks book",
    tags=TAGS,
    aliases=["hax"],
)

hacktricks.add_bookmark(
    "methodology",
    "https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-methodology",
    "pentesting methodology",
)

hacktricks.add_bookmark(
    "escalation",
    "https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist",
    "linux privilege escalation checklist",
)
