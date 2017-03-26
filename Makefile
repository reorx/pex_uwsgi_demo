export PEX_ENTRY ?= dist/$(shell basename $$PWD).pex

pex: clean
	@mkdir -p dist
	pex .  --disable-cache -r requirements.txt \
		-m amod.wsgi \
		-o $(PEX_ENTRY)

UWSGI_BIN ?= /Users/reorx/.venv/pex-demo/bin/uwsgi

run-amod:
	$(UWSGI_BIN) \
		--import loadpex.py \
		--module amod.wsgi:application \
		--master --workers 1 \
		--http :8000

run-bmod:
	$(UWSGI_BIN) \
		--import loadpex.py \
		--module bmod.wsgi:application \
		--master --workers 1 \
		--http :8001

.PHONY: build
build:
	python setup.py build

clean:
	rm -rf build dist *.egg-info
