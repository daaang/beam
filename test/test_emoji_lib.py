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

from beam.emoji_lib import sub_emoji
from beam.emoji_lib.duples import EMOJI_BY_NAME, EMOJI_BY_CHAR

class TestGitLogEmoji (unittest.TestCase):

    git_log_emoji = (
        ("⚡️", "zap"),              # Initial commit
        ("📚", "books"),            # Add data
        ("✅", "white_check_mark"), # Add feature/test
        ("🎨", "art"),              # Refactor tests
        ("💪", "muscle"),           # Refactor code
        ("💚", "green_heart"),      # Continuous integration
        ("📝", "memo"),             # Documentation
    )

    def test_emoji_by_name (self):
        for c, n in self.git_log_emoji:
            assert_that(EMOJI_BY_NAME[n], is_(equal_to(c)))

    def test_emoji_names_by_char (self):
        for c, n in self.git_log_emoji:
            assert_that(EMOJI_BY_CHAR[c], is_(equal_to(n)))

class TestSubEmoji (unittest.TestCase):

    def test_empty_str_yields_empty_str (self):
        assert_that(sub_emoji(""), is_(equal_to("")))

    def test_str_without_emoji_stays_the_same (self):
        assert_that(sub_emoji("un deux trois mon chat est bleu"),
                    is_(equal_to("un deux trois mon chat est bleu")))

    def test_art_emoji (self):
        assert_that(sub_emoji(":art:"), is_(equal_to("🎨")))

    def test_muscle_emoji (self):
        assert_that(sub_emoji(":muscle:"), is_(equal_to("💪")))

    def test_not_all_colons_are_emoji (self):
        assert_that(sub_emoji(":mattmattmatt:"),
                    is_(equal_to(":mattmattmatt:")))
        assert_that(sub_emoji(":hellohello:"),
                    is_(equal_to(":hellohello:")))

    def test_emoji_and_text (self):
        assert_that(sub_emoji("both :art: and :muscle: at once"),
                    is_(equal_to("both 🎨 and 💪 at once")))
