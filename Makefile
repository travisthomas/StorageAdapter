# Some helpers for build tooling

build:
	python3 setup.py bdist_wheel

clean: clean
	-rm -rf build dist *.egg-info
	# -rm -f $(DESTDIR)$(prefix)/bin/hello

.PHONY: build clean
