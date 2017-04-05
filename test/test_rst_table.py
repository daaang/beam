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
import unittest

from beam.rst_table import RstTable

class TableHelpers (unittest.TestCase):

    def init (self, spec):
        self.table = RstTable(spec)

    def add_header (self, *args):
        self.table.add_header(*args)

    def add_data (self, *args):
        self.table.add_data(*args)

    def assert_table (self, *args):
        assert_that(self.table, *args)

    def assert_no_header (self):
        assert_that(self.table.header, is_(none()))

    def assert_header_is (self, *args):
        assert_that(self.table.header, is_(equal_to(args)))

class GivenSingleLeftColumnTable (TableHelpers):

    def setUp (self):
        self.init("<")

class GivenSingleLeftColumnWithHeader (GivenSingleLeftColumnTable):

    def setUp (self):
        super().setUp()

        self.add_header("hello")

class GivenSingleLeftColumnWithOneRow (GivenSingleLeftColumnTable):

    def setUp (self):
        super().setUp()

        self.add_data("one")

class GivenTwoLeftColumnTable (TableHelpers):

    def setUp (self):
        self.init("<<")

class TestGivenNothing (TableHelpers):

    def test_can_set_ragged_left_column (self):
        self.init("><<")
        self.add_header("One", "Two", "Three")
        self.add_data("1", "Matt", "LaChance")

        assert_that(str(self.table), contains_string("\n  1 Matt"))

class TestSingleLeftColumnTable (GivenSingleLeftColumnTable):

    def test_is_empty (self):
        self.assert_table(has_length(0))

    def test_iterates_into_empty_list (self):
        assert_that(list(self.table), is_(equal_to([])))

    def test_has_no_header (self):
        self.assert_no_header()

    def test_cannot_add_two_column_header (self):
        assert_that(calling(self.add_header).with_args("hey",
                                                             "what"),
                    raises(TypeError))

    def test_str_is_empty (self):
        assert_that(str(self.table), is_(equal_to("")))

class TestSingleLeftColumnWithHeader (GivenSingleLeftColumnWithHeader):

    def test_is_empty (self):
        self.assert_table(has_length(0))

    def test_header_is_set (self):
        self.assert_header_is("hello")

    def test_has_no_header_after_deleting_header (self):
        del self.table.header
        self.assert_no_header()

    def test_str_is_empty (self):
        assert_that(str(self.table), is_(equal_to("")))

    def test_str_exists_when_given_data (self):
        self.add_data("example")
        assert_that(str(self.table),
                    is_(equal_to("=======\n hello\n=======\nexample\n=======")))

    def test_rule_factors_in_header (self):
        self.add_data("a")
        assert_that(str(self.table),
                    is_(equal_to("=====\nhello\n=====\na\n=====")))

class TestSingleLeftColumnWithOneRow (GivenSingleLeftColumnWithOneRow):

    def test_str_contains_data (self):
        assert_that(str(self.table), is_(equal_to("===\none\n===")))

    def test_new_data_changes_str (self):
        self.add_data("second")
        assert_that(str(self.table),
                    is_(equal_to("=======\none\nsecond\n=======")))

        self.add_data("third")
        assert_that(str(self.table),
                is_(equal_to("=======\none\nsecond\nthird\n=======")))

class TestTwoLeftColumnTable (GivenTwoLeftColumnTable):

    def test_is_empty (self):
        self.assert_table(has_length(0))

    def test_cannot_add_one_column_header (self):
        assert_that(calling(self.add_header).with_args("hey"),
                    raises(TypeError))

    def test_str_is_empty (self):
        assert_that(str(self.table), is_(equal_to("")))

    def test_str_exists_with_data (self):
        self.add_data("first", "second")
        assert_that(str(self.table),
                is_(equal_to("===== =======\nfirst second\n===== =======")))

        self.add_data("hi", "hi")
        assert_that(str(self.table), contains_string("\nhi    hi\n"))

        self.add_header("a", "b")
        assert_that(str(self.table), contains_string("\n  a      b\n"))

    def test_can_force_a_col_width (self):
        self.table.force_width(0, 1)
        self.add_data("hey", "what")
        assert_that(str(self.table),
                is_(equal_to("=== =====\nhey   what\n=== =====")))
