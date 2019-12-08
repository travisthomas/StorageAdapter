# Some helpers for build tooling

build:
	python3 setup.py bdist_wheel

install:
	python3 setup.py install

test: install
	python3 -m pytest test/

clean:
	-rm -rf build dist *.egg-info
	# -rm -f $(DESTDIR)$(prefix)/bin/hello

.PHONY: build install test clean
