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

class GivenSingleLeftColumnTable (unittest.TestCase):

    def setUp (self):
        self.table = RstTable("l")

class TestSingleLeftColumnTable (GivenSingleLeftColumnTable):

    def test_is_empty (self):
        assert_that(self.table, has_length(0))

    def test_has_no_header (self):
        assert_that(self.table.header, is_(none()))

    def test_can_add_header (self):
        self.table.add_header("hello")
        assert_that(self.table.header, is_(equal_to(("hello",))))
