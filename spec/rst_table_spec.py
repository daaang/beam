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

from beam.rst_table import RstTable

class Mod: pass

with description("an RstTable object"):
    with context("when initing with one left-aligned column"):
        with before.each:
            Mod.table = RstTable("<")

        with it("is empty"):
            assert_that(Mod.table, has_length(0))

        with it("iterates into an empty list"):
            assert_that(list(Mod.table), is_(equal_to([])))

        with it("has no header"):
            assert_that(Mod.table.header, is_(none()))

        with it("cannot add a two-column header"):
            assert_that(calling(Mod.table.add_header).with_args("hey",
                                                                "what"),
                        raises(TypeError))

        with it("converts to an empty str"):
            assert_that(str(Mod.table), is_(equal_to("")))

        with context("and it's given a header"):
            with before.each:
                Mod.table.add_header("hello")

            with it("is empty"):
                assert_that(Mod.table, has_length(0))

            with it("remembers its header"):
                assert_that(Mod.table.header, is_(equal_to(("hello",))))

            with it("has no header after deleting the header"):
                del Mod.table.header
                assert_that(Mod.table.header, is_(none()))

            with it("converts to an empty str"):
                assert_that(str(Mod.table), is_(equal_to("")))

            with it("has a str when given data"):
                Mod.table.add_data("example")
                assert_that(str(Mod.table),
                            is_(equal_to("=======\n"
                                         " hello\n"
                                         "=======\n"
                                         "example\n"
                                         "=======")))

            with it("pays attention to the header for rule length"):
                Mod.table.add_data("a")
                assert_that(str(Mod.table),
                            is_(equal_to("=====\n"
                                         "hello\n"
                                         "=====\n"
                                         "a\n"
                                         "=====")))

        with context("and it's given one row"):
            with before.each:
                Mod.table.add_data("one")

            with it("contains that row"):
                assert_that(str(Mod.table),
                            is_(equal_to("===\none\n===")))

            with context("and it's given a second row"):
                with before.each:
                    Mod.table.add_data("second")

                with it("contains both rows"):
                    assert_that(str(Mod.table),
                                is_(equal_to("=======\n"
                                             "one\n"
                                             "second\n"
                                             "=======")))

                with it("will contain a third added row"):
                    Mod.table.add_data("third")
                    assert_that(str(Mod.table),
                                is_(equal_to("=======\n"
                                             "one\n"
                                             "second\n"
                                             "third\n"
                                             "=======")))

    with context("when initing with two left-aligned columns"):
        with before.each:
            Mod.table = RstTable("<<")

        with it("is empty"):
            assert_that(Mod.table, has_length(0))

        with it("cannot add a one-column header"):
            assert_that(calling(Mod.table.add_header).with_args("hey"),
                        raises(TypeError))

        with it("converts to an empty str"):
            assert_that(str(Mod.table), is_(equal_to("")))

        with context("and it's given one row"):
            with before.each:
                Mod.table.add_data("first", "second")

            with it("converts to a nonempty str"):
                assert_that(str(Mod.table),
                            is_(equal_to("===== =======\n"
                                         "first second\n"
                                         "===== =======")))

            with it("a second row with short items indents them"):
                Mod.table.add_data("hi", "hi")
                assert_that(str(Mod.table),
                            contains_string("\nhi    hi\n"))

            with it("a header will indent to centered"):
                Mod.table.add_header("a", "b")
                assert_that(str(Mod.table),
                            contains_string("\n  a      b\n"))

        with context("and its first col is given a width of 1"):
            with before.each:
                Mod.table.force_width(0, 1)

            with it("treates longer cells as having len=1"):
                Mod.table.add_data("hey", "what")
                assert_that(str(Mod.table),
                            is_(equal_to("=== =====\n"
                                         "hey   what\n"
                                         "=== =====")))

    with it("can be inited with a ragged left column"):
        table = RstTable("><<")
        table.add_header("One", "Two", "Three")
        table.add_data("1", "Matt", "LaChance")

        assert_that(str(table), contains_string("\n  1 Matt"))
