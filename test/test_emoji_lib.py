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

from beam.emoji_lib import EMOJI_BY_NAME, EMOJI_BY_CHAR

class TestGitLogEmoji (unittest.TestCase):

    git_log_emoji = (
        ("⚡️", "zap"),              # Initial commit
        ("📚", "books"),            # Add data
        ("✅", "white_check_mark"), # Add feature/test
        ("🎨", "art"),              # Refactor tests
        ("💚", "green_heart"),      # Continuous integration
        ("📝", "memo"),             # Documentation
    )

    def test_emoji_by_name (self):
        for c, n in self.git_log_emoji:
            assert_that(EMOJI_BY_NAME[n], is_(equal_to(c)))

    def test_emoji_names_by_char (self):
        for c, n in self.git_log_emoji:
            assert_that(EMOJI_BY_CHAR[c], is_(equal_to(n)))
