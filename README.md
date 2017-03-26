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

## Develop

### Setup Environment

```
# create virtualenv
mkvirtualenv pex-demo

# install `params`, `getenv` required by `amod` and `bmod`
pip install -r requirements.txt

# install `pex`, `uwsgi` required in development process
pip install -r dev-requirements.txt
```


### Pack

```bash
pex .  --disable-cache \
	-r requirements.txt \
	-m amod.wsgi \
	-o dist/$$(basename $$PWD).pex
```


### Run

**amod**:

```bash
PEX_ENTRY=dist/pex_uwsgi_demo.pex /Users/reorx/.venv/pex-demo/bin/uwsgi \
	--import loadpex.py \
	--module amod.wsgi:application \
	--master --workers 1 \
	--http :8000
```

> $ make run-amod

**bmod**:

```bash
PEX_ENTRY=dist/pex_uwsgi_demo.pex /Users/reorx/.venv/pex-demo/bin/uwsgi \
	--import loadpex.py \
	--module bmod.wsgi:application \
	--master --workers 1 \
	--http :8001
```

> $ make run-bmod

## Deploy

### Server Environment

Server requires:

- Python 2.7
- uWSGI executable
- `loadpex.py` script

```
pip install uwsgi

curl https://github.com/reorx/pex_uwsgi_demo/raw/master/loadpex.py -L -o loadpex.py
```

### Run

Transfer packed `pex_uwsgi_demo.pex` to server, then run:

```
PEX_ENTRY=pex_uwsgi_demo.pex uwsgi \
	--import loadpex.py \
	--module amod.wsgi:application \
	--master --workers 1 \
	--http :8000
```
