# PEX uWSGI Packaging Demo

- PEX: https://github.com/pantsbuild/pex, https://pex.readthedocs.io/en/stable/
- uWSGI: https://uwsgi-docs.readthedocs.io/en/latest/


## Hierarchy

```
pex_uwsgi_demo
├── amod
│   ├── __init__.py
│   └── wsgi.py
├── bmod
│   ├── __init__.py
│   └── wsgi.py
├── dist
│   └── pex_uwsgi_demo.pex
├── Makefile
├── README.md
├── loadpex.py
├── requirements.txt
└── setup.py
```


## Pack

```bash
pex .  --disable-cache \
	-r requirements.txt \
	-m amod.wsgi \
	-o dist/$$(basename $$PWD).pex
```


## Run

**amod**:

```bash
PEX_ENTRY=dist/pex_uwsgi_demo.pex /Users/reorx/.venv/pex-demo/bin/uwsgi \
	--import loadpex.py \
	--module amod.wsgi:application \
	--http :8000
```

> $ make run-amod

**bmod**:

```bash
PEX_ENTRY=dist/pex_uwsgi_demo.pex /Users/reorx/.venv/pex-demo/bin/uwsgi \
	--import loadpex.py \
	--module bmod.wsgi:application \
	--http :8000
```

> $ make run-bmod
