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
from hamcrest import *

from beam.lilconf.shell_generation.structures import BaseStructure

class Mod:
    pass

with description("default BaseStructure object"):
    with before.each:
        Mod.structure = BaseStructure()

    with it("evaluates to false"):
        assert_that(bool(Mod.structure), is_(equal_to(False)))

    with it("converts to an empty str"):
        assert_that(Mod.structure, has_string(""))

    with it("has an empty indent str"):
        assert_that(Mod.structure.indent, is_(equal_to("")))

    with it("has a two-space tab"):
        assert_that(Mod.structure.tab, is_(equal_to("  ")))

    with it("doesn't allow indent deletion"):
        assert_that(calling(delattr).with_args(Mod.structure, "indent"),
                    raises(NotImplementedError))

    with it("doesn't allow tab deletion"):
        assert_that(calling(delattr).with_args(Mod.structure, "tab"),
                    raises(NotImplementedError))

    with context("when setting a new indent"):
        with before.each:
            Mod.structure.indent = "tabtabtab"

        with it("remembers its indent"):
            assert_that(Mod.structure.indent,
                        is_(equal_to("tabtabtab")))

        with it("still converts to an empty str"):
            assert_that(Mod.structure, has_string(""))

    with context("when setting a new tab"):
        with before.each:
            Mod.structure.tab = "\t"

        with it("remembers its tab"):
            assert_that(Mod.structure.tab, is_(equal_to("\t")))

        with it("still has an empty indent"):
            assert_that(Mod.structure.indent, is_(equal_to("")))

        with it("still converts to an empty str"):
            assert_that(Mod.structure, has_string(""))
