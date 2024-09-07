# Scholar Public Repository

This is (most) of the codex definitions for the public instance of
[scholar](https://github.com/adammillerio/sch), which is hosted at https://sch.luphy.net

# Getting Started

First install [scholar](https://github.com/adammillerio/sch).

Then, install this repository with pip:
```bash
pip install 'https://github.com/adammillerio/sch_public/archive/main.zip'
```

To load all codexes, just add the import to `app.py`:
```python
from sch_public.codexes.codexes import __name__
```

Or just add a specific codex:
```python
from sch_public.codexes.code import __name__
```

# Development

Install in development mode:
```bash
pip3 install -e '.[dev]'
```

## Type Checking

Ensure no type errors are present with [pyre](https://github.com/facebook/pyre-check):

```bash
pyre check              
ƛ No type errors found
```

**Note**: Pyre daemonizes itself on first run for faster subsequent executions. Be
sure to shut it down with `pyre kill` when finished.

## Formatting

Format code with the [ruff](https://github.com/astral-sh/ruff) formatter:

```bash
ruff format
27 files left unchanged
```
