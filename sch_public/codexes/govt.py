#!/usr/bin/env python3
from sch import codex

TAGS = ["public", "govt"]


@codex.command("usps", tags=TAGS)
def usps(*args: str) -> str:
    """track packages

    All arguments are unpacked into a csv submitted as tLabels.

    if args:
        return https://tools.usps.com/go/TrackConfirmAction?tLabels={*args}
    else:
        return https://www.usps.com/
    """

    if args:
        labels = ",".join(args)

        return f"https://tools.usps.com/go/TrackConfirmAction?tLabels={labels}"
    else:
        return "https://www.usps.com/"


@codex.command("ups")
def ups(tracking: str) -> str:
    return f"https://www.ups.com/track?loc=en_US&requester=QUIC&tracknum={tracking}/trackdetails"
