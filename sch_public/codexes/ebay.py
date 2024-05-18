#!/usr/bin/env python3
from sch import codex, query_args

TAGS = ["shopping"]


@codex.command("ebay", tags=TAGS)
def ebay(*args: str) -> str:
    """ebay marketplace

    if args:
        return https://www.ebay.com/sch/i.html?_nkw={*args}
    else:
        return https://ebay.com
    """

    if args:
        return f"https://www.ebay.com/sch/i.html?_nkw={query_args(*args)}"
    else:
        return "https://ebay.com"
