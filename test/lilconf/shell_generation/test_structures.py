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

from beam.lilconf.shell_generation.structures import BaseStructure

class ObjectWithStructure:

    def assert_str (self, expected_str):
        assert_that(self.structure, has_string(expected_str))

    def assert_cannot_delete (self, attr):
        assert_that(calling(delattr).with_args(self.structure, attr),
                    raises(NotImplementedError))

    def get_indent (self):
        return self.structure.indent

    def set_indent (self, value):
        self.structure.indent = value

    def get_tab (self):
        return self.structure.tab

    def set_tab (self, value):
        self.structure.tab = value

class TestBaseStructure (ObjectWithStructure, unittest.TestCase):

    def setUp (self):
        self.structure = BaseStructure()

    def test_evaluates_to_false (self):
        assert_that(bool(self.structure), is_(equal_to(False)))

    def test_str_is_empty (self):
        self.assert_str("")

    def test_default_indent_is_empty_str (self):
        assert_that(self.get_indent(), is_(equal_to("")))

    def test_default_tab_is_two_spaces (self):
        assert_that(self.get_tab(), is_(equal_to("  ")))

    def test_when_setting_indent_str_is_still_empty (self):
        self.set_indent("    ")
        assert_that(self.get_indent(), is_(equal_to("    ")))
        self.assert_str("")

    def test_can_set_tab (self):
        self.set_tab("\t")
        assert_that(self.get_tab(), is_(equal_to("\t")))

    def test_cannot_delete_indent (self):
        self.assert_cannot_delete("indent")

    def test_cannot_delete_tab (self):
        self.assert_cannot_delete("tab")
