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

from lilconf.shell_generation.structures import Assignment

class GivenNothing (unittest.TestCase):

    def test_simple_strs (self):
        structure = Assignment("var", "'value'")
        assert_that(structure, has_string("var='value'"))

    def test_more_strs (self):
        structure = Assignment("hey", '"what\'s up"')
        assert_that(structure, has_string("hey=\"what's up\""))
