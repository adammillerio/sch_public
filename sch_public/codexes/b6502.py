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

b6502.add_bookmark("clock", "https://eater.net/8bit/clock", "clock kit guide")

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
