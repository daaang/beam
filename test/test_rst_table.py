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

    def assert_table (self, *args):
        assert_that(self.table, *args)

    def assert_no_header (self):
        assert_that(self.table.header, is_(none()))

    def assert_header_is (self, *args):
        assert_that(self.table.header, is_(equal_to(args)))

class GivenSingleLeftColumnTable (TableHelpers):

    def setUp (self):
        self.table = RstTable("l")

class GivenSingleLeftColumnWithHeader (GivenSingleLeftColumnTable):

    def setUp (self):
        super().setUp()

        self.table.add_header("hello")

class GivenTwoLeftColumnTable (TableHelpers):

    def setUp (self):
        self.table = RstTable("ll")

class TestSingleLeftColumnTable (GivenSingleLeftColumnTable):

    def test_is_empty (self):
        self.assert_table(has_length(0))

    def test_iterates_into_empty_list (self):
        assert_that(list(self.table), is_(equal_to([])))

    def test_has_no_header (self):
        self.assert_no_header()

    def test_cannot_add_two_column_header (self):
        assert_that(calling(self.table.add_header).with_args("hey",
                                                             "what"),
                    raises(TypeError))

    def test_can_add_data_row (self):
        self.table.add_data("one")

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

class TestTwoLeftColumnTable (GivenTwoLeftColumnTable):

    def test_is_empty (self):
        self.assert_table(has_length(0))

    def test_cannot_add_one_column_header (self):
        assert_that(calling(self.table.add_header).with_args("hey"),
                    raises(TypeError))
