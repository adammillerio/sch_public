#!/usr/bin/env python3
from typing import Optional
from urllib.parse import urljoin, urlparse

from sch import codex, query_args

codex.add_bookmark(
    "chef",
    "https://gchq.github.io/CyberChef/",
    "cyberchef data manipulation tool",
    tags=["public", "tools", "code"],
)


@codex.command("archive", tags=["public", "tools", "code"])
def archive(url: Optional[str] = None, version: str = "newest") -> str:
    """view archive.ph for provided url

    All query args will be in the URL will be removed, since they usually cause
    issues with finding existing archives.

    Optionally a version can be provided, the only available version currently
    is "oldest".

    if url:
        if version:
            return https://archive.ph/{version}/{url}
        else:
            return https://archive.ph/newest/{url}
    else:
        return https://archive.ph
    """

    if url:
        # Remove query args.
        url_parse = urlparse(url)
        url = urljoin(url, url_parse.path)

        return f"https://archive.is/{version.lower()}/{query_args(url)}"
    else:
        return "https://archive.is"
