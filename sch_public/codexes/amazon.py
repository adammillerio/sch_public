#!/usr/bin/env python3
from typing import List

from sch import codex, Command

TAGS = ["public", "amazon"]


SHOPPING_TAGS: List[str] = TAGS + ["shopping"]


amazon: Command = codex.add_search(
    "amazon",
    "https://amazon.com/s/?field-keywords=",
    "https://amazon.com",
    "search or go to amazon",
    tags=SHOPPING_TAGS,
)


amazon.add_bookmark(
    "orders", "https://www.amazon.com/gp/your-account/order-history", "order history"
)

amazon.add_bookmark("cart", "https://www.amazon.com/gp/cart/view.html", "shopping cart")


STREAMING_TAGS: List[str] = TAGS + ["streaming"]
codex.add_bookmark(
    "twitch", "https://twitch.tv", "twitch video streaming", tags=STREAMING_TAGS
)
