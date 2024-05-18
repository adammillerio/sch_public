#!/usr/bin/env python3
from typing import List

from sch import codex, query_args

TAGS = ["public", "amazon"]


SHOPPING_TAGS: List[str] = TAGS + ["shopping"]


@codex.command("amazon", tags=SHOPPING_TAGS)
def amazon(*args: str) -> str:
    """search or go to amazon

    if args:
        return https://amazon.com/s/?field-keywords={*args}
    else:
        return https://amazon.com
    """

    if args:
        return f"https://amazon.com/s/?field-keywords={query_args(*args)}"
    else:
        return "https://amazon.com"


amazon.add_bookmark(
    "orders", "https://www.amazon.com/gp/your-account/order-history", "order history"
)

amazon.add_bookmark("cart", "https://www.amazon.com/gp/cart/view.html", "shopping cart")


STREAMING_TAGS: List[str] = TAGS + ["streaming"]
codex.add_bookmark(
    "twitch", "https://twitch.tv", "twitch video streaming", tags=STREAMING_TAGS
)
