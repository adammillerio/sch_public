#!/usr/bin/env python3
# ruff: noqa: F401

from sch import codex, CodexServer

from sch_public.codexes.codexes import __name__


@codex.command(name="hello", tags=["public"])
def hello() -> str:
    return "https://github.com/adammillerio/sch"


# Flask Application Factory
# Run with flask --app example_codex run
def create_app() -> CodexServer:
    return codex.create_app()
