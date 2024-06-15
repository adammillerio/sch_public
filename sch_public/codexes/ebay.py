#!/usr/bin/env python3
from sch import codex, Command

TAGS = ["public", "shopping"]


ebay: Command = codex.add_search(
    "ebay",
    "https://www.ebay.com/sch/i.html?_nkw=",
    "https://ebay.com",
    "ebay marketplace",
    tags=TAGS,
)

ebay.add_search(
    "orders",
    "https://www.ebay.com/mye/myebay/purchase?mp=purchase-search-module-v2&type=v2&pg=purchase&q=",
    "https://www.ebay.com/mye/myebay/purchase",
    "orders",
    escaped=True,
)
