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

from beam.emoji_lib import EMOJI_BY_NAME

EMOJI_SO_FAR = (
    ("⚡️", "zap"),
    ("📚", "books"),
    ("✅", "white_check_mark"),
)

class TestNothing (unittest.TestCase):

    def test_emoji_by_name (self):
        for c, n in EMOJI_SO_FAR:
            assert_that(EMOJI_BY_NAME[n], is_(equal_to(c)))
