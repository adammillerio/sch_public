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
