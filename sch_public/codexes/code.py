#!/usr/bin/env python3
from typing import Callable, Optional, NamedTuple, Iterable

from pyre_extensions import none_throws

from sch import codex, command, Command, format_doc, query_args


TAGS = ["public", "code"]


class Repo(NamedTuple):
    name: str
    docs: str
    errors: Optional[str] = None
    tags: Optional[Iterable[str]] = None


repos = {
    "invoke": Repo(
        name="pyinvoke/invoke",
        docs="https://docs.pyinvoke.org/en/stable",
    ),
    "click": Repo(
        name="pallets/click",
        docs="https://click.palletsprojects.com/en/8.1.x",
    ),
    "flask": Repo(
        name="pallets/flask",
        docs="https://flask.palletsprojects.com/en/3.0.x",
    ),
    "luigi": Repo(
        name="spotify/luigi",
        docs="https://flask.palletsprojects.com/en/3.0.x",
    ),
    "hammerspoon": Repo(
        name="Hammerspoon/hammerspoon",
        docs="https://www.hammerspoon.org/docs",
    ),
    "buck": Repo(
        name="facebook/buck2",
        docs="https://buck2.build/docs",
    ),
    "sapling": Repo(
        name="facebook/sapling", docs="https://sapling-scm.com/docs/introduction"
    ),
    "pyre": Repo(
        name="facebook/pyre-check",
        docs="https://pyre-check.org/docs/getting-started/",
        errors="https://pyre-check.org/docs/errors/",
    ),
    "beets": Repo(name="beetbox/beets", docs="https://beets.readthedocs.io/en/stable"),
    "rockbox": Repo(
        name="Rockbox/rockbox",
        docs="https://download.rockbox.org/daily/manual/rockbox-ipod6g/rockbox-build.html",
    ),
    "anytree": Repo(
        name="c0fec0de/anytree", docs="https://anytree.readthedocs.io/en/stable/"
    ),
    "tup": Repo(name="gittup/tup", docs="https://gittup.org/tup/"),
    "jupyterlab": Repo(
        name="jupyterlab/jupyterlab",
        docs="https://jupyterlab.readthedocs.io/en/latest/",
    ),
    "logisim": Repo(
        name="logisim-evolution/logisim-evolution",
        docs="https://github.com/logisim-evolution/logisim-evolution/blob/main/docs/docs.md",
        tags=["6502"],
    ),
}


def github_search_url(repo: str, *args: str) -> str:
    query = query_args(f"repo:{repo}", *args)

    return f"https://github.com/search?type=code&q={query}"


@codex.command("gh", tags=TAGS)
def github(repo: Optional[str] = None) -> str:
    """go to github or a view a repo

    if repo:
        return https://github.com/{repo}
    else:
        return https://github.com
    """

    if repo:
        return f"https://github.com/{repo}"
    else:
        return "https://github.com"


@github.command("search")
def github_search(repo: str, *args: str) -> str:
    """search a github repo

    return https://github.com/search?type=code&q=repo:{repo}+{*args}
    """

    return github_search_url(repo, *args)


@github_search.command("all")
def github_search_all(*args: str) -> str:
    """search all of github

    return https://github.com/search?type=code&q={*args}
    """

    return f"https://github.com/search?type=code&q={query_args(*args)}"


def code_command(
    repo_name: str,
    repo_docs: str,
    repo_errors: Optional[str] = None,
    repo_tags: Optional[Iterable[str]] = None,
) -> Command:
    if repo_tags:
        tags = set(repo_tags)
        tags.add("public")
        tags.add("code")
    else:
        tags = TAGS

    @command(tags=tags)
    @format_doc(repo_name=repo_name)
    def code_repo(*args: str) -> str:
        """{repo_name} on github

        if args:
            return https://github.com/search?type=code&q=repo:{repo_name}+{{*args}}
        else:
            return https://github.com/{repo_name}
        """

        if args:
            return github_search_url(repo_name, *args)
        else:
            return f"https://github.com/{repo_name}"

    @code_repo.command("docs")
    @format_doc(repo_docs=repo_docs)
    def code_repo_docs() -> str:
        """hosted docs

        return {repo_docs}
        """

        return repo_docs

    @code_repo.command("file")
    @format_doc(repo_name=repo_name)
    def code_repo_file(file_str: str) -> str:
        """file search

        return https://github.com/{repo_name}/tree/main/{{file_str}}
        """

        return f"https://github.com/{repo_name}/tree/main/{file_str}"

    @code_repo.command("prs")
    @format_doc(repo_name=repo_name)
    def code_repo_pr(pr: Optional[str] = None) -> str:
        """go to pr or view prs

        if pr:
            return https://github.com/{repo_name}/pull/{{pr}}
        else:
            return https://github.com/{repo_name}/pulls
        """

        if pr:
            return f"https://github.com/{repo_name}/pull/{pr}"
        else:
            return f"https://github.com/{repo_name}/pulls"

    @code_repo.command("issues")
    @format_doc(repo_name=repo_name)
    def code_repo_issue(issue: Optional[str] = None) -> str:
        """go to issue or view issues

        if issue:
            return https://github.com/{repo_name}/issues/{{issue}}
        else:
            return https://github.com/{repo_name}/issues
        """

        if issue:
            return f"https://github.com/{repo_name}/issues/{issue}"
        else:
            return f"https://github.com/{repo_name}/issues"

    if repo_errors is not None:

        @code_repo.command("errors")
        @format_doc(repo_name=repo_name, repo_errors=repo_errors)
        def code_repo_errors(issue: Optional[str] = None) -> str:
            """main error troubleshooting page

            return {repo_errors}
            """

            return none_throws(repo_errors)

    return code_repo


for name, config in repos.items():
    codex.add_command(code_command(*config), name)


codex.add_bookmark("sourcehut", "https://sr.ht/", "sourcehut git host", tags=TAGS)


@codex.command("commonmark", tags=TAGS)
def commonmark() -> str:
    """commonmark spec

    All md -> html/txt formatting in sch is done via the commonmark_x engine in
    pandoc, so this is the spec which all md docs should adhere to.

    For info on pandoc's use of CommonMark, see sch pandoc commonmark_x

    return https://spec.commonmark.org/current/
    """

    return "https://spec.commonmark.org/current/"


pandoc: Command = codex.add_command(
    code_command("jgm/pandoc", "https://pandoc.org"), "pandoc"
)


@pandoc.command("commonmark_x")
def pandoc_commonmark_x() -> str:
    """commonmark_x extension definition

    commonmark_x is separate from the commonmark engine in that it includes several
    useful pandoc extensions which add more functionality than what is provided
    in commonmark. This is the list of extensions currently enabled, which can
    also be used when rendering pages in sch.

    Search the extension name in the manual (sch pandoc manual) to learn more
    about extension functionality.

    return https://github.com/jgm/pandoc/blob/509cc3ac8765f3d531f953e5ef7a24901bce0ec7/src/Text/Pandoc/Extensions.hs#L410
    """

    return "https://github.com/jgm/pandoc/blob/509cc3ac8765f3d531f953e5ef7a24901bce0ec7/src/Text/Pandoc/Extensions.hs#L410"


pandoc.add_bookmark(
    "manual", "https://pandoc.org/MANUAL.html", "pandoc CLI manual", tags=TAGS
)

codex.add_bookmark("regex", "https://regex101.com", "regex 101 regex tester", tags=TAGS)

solarized: Command = codex.add_bookmark(
    "solarized",
    "https://en.wikipedia.org/wiki/Solarized",
    "solarized color pallette",
    tags=TAGS,
)

solarized.add_bookmark(
    "css",
    "https://thomasf.github.io/solarized-css/",
    "css stylesheet",
)


python: Command = codex.add_search(
    "python",
    "https://docs.python.org/3/search.html?q=",
    "https://docs.python.org/3/",
    "python programming language",
)


python.add_bookmark("match", "https://peps.python.org/pep-0636/", "pattern matching")
python.add_bookmark(
    "functional", "https://docs.python.org/3/howto/functional.html", "functional howto"
)


pypi: Command = codex.add_search(
    "pypi", "https://pypi.org/search/?q=", "https://pypi.org/", "python_package_index"
)

pypi.add_bookmark(
    "classifiers", "https://pypi.org/classifiers/", "python package classifiers"
)

jupyter: Command = codex.add_command(
    code_command(
        "jupyter/notebook", "https://jupyter-notebook.readthedocs.io/en/stable/"
    ),
    "jupyter",
)
