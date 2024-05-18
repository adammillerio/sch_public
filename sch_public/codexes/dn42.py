#!/usr/bin/env python3
from sch import codex, query_args

TAGS = ["lab", "network", "dn42", "project"]


@codex.command("dn42", tags=TAGS)
def dn42(*args: str) -> str:
    """dn42 "simulated" internet VPN project

    This is basically just using VPN stuff like wireguard/openvpn/ipsec to run
    their own "internet", with their own BGP, whois, ASNs, DNS, etc.
    """

    if args:
        return f"https://wiki.dn42.us/search?q={query_args(*args)}"
    else:
        return "https://wiki.dn42.us/Home"


dn42.add_bookmark(
    "guide", "https://wiki.dn42.us/howto/Getting-Started", "onboarding guide", tags=TAGS
)
