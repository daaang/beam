# lilconf: Li'l Configure
# Copyright 2017 Matt LaChance
#
# This file is part of lilconf.
#
# lilconf is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# lilconf is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with lilconf. If not, see <http://www.gnu.org/licenses/>.
from hamcrest import *
import unittest

from lilconf.shell_generation.structures import BaseStructure

class ObjectWithStructure:

    def assert_str (self, expected_str):
        assert_that(self.structure, has_string(expected_str))

class TestBaseStructure (ObjectWithStructure, unittest.TestCase):

    def setUp (self):
        self.structure = BaseStructure()

    def test_evaluates_to_false (self):
        assert_that(bool(self.structure), is_(equal_to(False)))

    def test_str_is_empty (self):
        self.assert_str("")

    def test_default_indent_is_empty_str (self):
        assert_that(self.structure.get_indent(), is_(equal_to("")))

    def test_default_tab_is_two_spaces (self):
        assert_that(self.structure.get_tab(), is_(equal_to("  ")))

    def test_when_setting_indent_str_is_still_empty (self):
        self.structure.set_indent("    ")
        assert_that(self.structure.get_indent(), is_(equal_to("    ")))
        assert_that(self.structure, has_string(""))

    def test_can_set_tab (self):
        self.structure.set_tab("\t")
