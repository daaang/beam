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

from lilconf.shell_generation.structures import \
        ShellAssignment, \
        ShellCommand, \
        ShellSequence

class AssignmentTest (unittest.TestCase):

    def test_simple_strs (self):
        structure = ShellAssignment("var", "'value'")
        assert_that(structure, has_string("var='value'"))

    def test_more_strs (self):
        structure = ShellAssignment("hey", '"what\'s up"')
        assert_that(structure, has_string("hey=\"what's up\""))

class CommandTest (unittest.TestCase):

    def test_can_write_command (self):
        structure = ShellCommand("cat", "some_file.txt")
        assert_that(structure, has_string("cat some_file.txt"))

    def test_can_write_simple_true_command (self):
        assert_that(ShellCommand("true"),
                    has_string("true"))

class SequenceTest (unittest.TestCase):

    def test_can_create_sequence (self):
        structure = ShellSequence("some line")
        assert_that(structure, has_string("some line"))

    def test_can_create_sequence_of_one (self):
        structure = ShellSequence("cut -f1 some_file.txt")
        assert_that(structure, has_string("cut -f1 some_file.txt"))

    def test_can_have_a_sequence_of_two (self):
        structure = ShellSequence("first line", "second line")
        assert_that(structure, has_string("first line\nsecond line"))

    def test_cannot_init_sequence_of_zero (self):
        assert_that(calling(ShellSequence), raises(TypeError))

    def test_can_create_sequence_of_assignments (self):
        structure = ShellSequence(
                ShellAssignment("a", "'bibbity'"),
                ShellAssignment("b", "'bobbity'"),
                ShellAssignment("c", "'boo'"))
        assert_that(structure,
                    has_string("a='bibbity'\nb='bobbity'\nc='boo'"))
