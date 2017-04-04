# beam: Scripts for Me
# Copyright 2017 Matt LaChance
#
# This file is part of beam.
#
# beam is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# beam is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with beam. If not, see <http://www.gnu.org/licenses/>.
PYTHON3=python3
SETUP=$(PYTHON3) setup.py

build: setup.py
	$(SETUP) build

dist: build
	$(SETUP) sdist
	$(SETUP) bdist_wheel

.PHONY: install clean test

install: build
	$(SETUP) install

clean:
	-rm -r lib/beam.egg-info build dist
	-find . -name '*.c' | xargs rm
	-find . -name __pycache__ | xargs rm -r

test: clean build
	(for libdir in build/lib*; do \
	  echo "PYTHONPATH=\"$$libdir\""; \
	  PYTHONPATH="$$libdir" $(PYTHON3) -m unittest || exit; done)
	find test -name '*.bats' | xargs bats
	$(MAKE) clean
