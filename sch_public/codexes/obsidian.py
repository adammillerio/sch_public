from sch import codex

TAGS = ["obsidian", "docs"]


@codex.command("obsidian", tags=TAGS)
def obsidian() -> str:
    """obsidian note taking app

    return https://help.obsidian.md/Home
    """

    return "https://help.obsidian.md/Home"


@obsidian.command("uri")
def obsidian_uri() -> str:
    """obsidian uri reference

    sch uses Obsidian URIs to generate redirect links to notes inside of the
    Obsidian vault.

    return https://help.obsidian.md/Extending+Obsidian/Obsidian+URI
    """

    return "https://help.obsidian.md/Extending+Obsidian/Obsidian+URI"
