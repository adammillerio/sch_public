#!/usr/bin/env python3
from sch import codex, Command


TAGS = ["public", "project", "code", "6502"]

b6502: Command = codex.add_bookmark(
    "6502",
    "https://eater.net/6502",
    "ben eater 6502 project",
    tags=TAGS,
    aliases=["eater"],
)

b6502.add_bookmark("start", "https://eater.net/start", "kit starter guides")

b6502_breadboarding: Command = b6502.add_bookmark(
    "breadboarding",
    "https://www.youtube.com/watch?v=PE-_rJqvDhQ",
    "breadboarding tips & tricks",
)

b6502_clock: Command = b6502.add_bookmark(
    "clock", "https://eater.net/8bit/clock", "clock kit guide"
)

b6502_clock.add_bookmark(
    "schematic", "https://eater.net/schematics/clock.png", "circuit diagram"
)

b6502_clock.add_bookmark(
    "latch",
    "https://www.youtube.com/watch?v=KM0DdEaY5sY",
    "detailed sr latch explanation",
)

b6502_clock_video: Command = b6502_clock.add_bookmark(
    "video",
    "https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU",
    "8-bit computer playlist (includes clock)",
)

b6502_clock_video_1: Command = b6502_clock_video.add_bookmark(
    "1",
    "https://www.youtube.com/watch?v=kRlSFm519Bo",
    "astable 555 timer - 8-bit computer clock - part 1",
)
b6502_clock_video_1_circuit: Command = b6502_clock_video_1.add_bookmark(
    "circuit", "https://www.falstad.com/circuit/e-555square.html", "circuit simulation"
)
b6502_clock_video_1_circuit.add_bookmark(
    "internals", "https://www.falstad.com/circuit/e-555int.html", "circuit internals"
)

b6502_clock_video.add_bookmark(
    "2",
    "https://www.youtube.com/watch?v=81BgFhm2vz8",
    "monostable 555 timer - 8-bit computer clock - part 2",
)
b6502_clock_video.add_bookmark(
    "3",
    "https://www.youtube.com/watch?v=WCwJNnx36Rk",
    "bistable 555 - 8-bit computer clock - part 3",
)
b6502_clock_video.add_bookmark(
    "4",
    "https://www.youtube.com/watch?v=SmQ5K7UQPMM",
    "clock logic - 8-bit computer clock - part 4",
)

datasheets: Command = codex.add_bookmark(
    "datasheets",
    "/sch?s=datasheets+sch_tree",
    "chip datasheets",
    tags=TAGS,
    aliases=["ds"],
)

ds_infos = [
    ("lm555", "https://eater.net/datasheets/lm555.pdf"),
    ("74ls04", "https://eater.net/datasheets/74ls04.pdf"),
    ("74ls08", "https://eater.net/datasheets/74ls08.pdf"),
    ("74ls32", "https://eater.net/datasheets/74ls32.pdf"),
]
for ds in ds_infos:
    datasheets.add_bookmark(ds[0], ds[1], f"datasheet for {ds[0]}")

b6502.add_bookmark(
    "instructions",
    "https://www.masswerk.at/6502/6502_instruction_set.html",
    "instruction set",
)

b6502.add_bookmark("tutorials", "http://www.6502.org/tutorials/", "6502.org tutorials")

b6502.add_bookmark("sim", "https://natecatelli.com/bes/", "ben eater 6502 sim")

codex.add_bookmark(
    "minipro",
    "https://gitlab.com/DavidGriffith/minipro",
    "oss tl86xx chip programmer tool",
    tags=TAGS,
)

codex.add_bookmark(
    "circuit",
    "https://www.falstad.com/circuit/",
    "web based digital logic sim",
    tags=TAGS,
)
