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

from beam.emoji_lib import sub_emoji, sub_emoji_term_io
from beam.emoji_lib.duples import EMOJI_BY_NAME, EMOJI_BY_CHAR

git_log_emoji = (
    ("⚡️", "zap"),
    ("📚", "books"),
    ("✅", "white_check_mark"),
    ("🎨", "art"),
    ("💪", "muscle"),
    ("💚", "green_heart"),
    ("📝", "memo"),
)

with description("our emoji index"):
    with it("can find emoji by name"):
        for c, n in git_log_emoji:
            assert_that(EMOJI_BY_NAME[n], is_(equal_to(c)))

    with it("can find emoji name by char"):
        for c, n in git_log_emoji:
            assert_that(EMOJI_BY_CHAR[c], is_(equal_to(n)))

with description("the sub_emoji() method"):
    with it("leaves the empty str alone"):
        assert_that(sub_emoji(""),
                    is_(equal_to("")))

    with it("leaves alone a str without emoji"):
        assert_that(sub_emoji("un deux trois mon chat est bleu"),
                    is_(equal_to("un deux trois mon chat est bleu")))

    with it("ignores colons which are not emoji"):
        assert_that(sub_emoji(":mattmattmatt:"),
                    is_(equal_to(":mattmattmatt:")))
        assert_that(sub_emoji(":hellohello:"),
                    is_(equal_to(":hellohello:")))

    with it("translates :art:"):
        assert_that(sub_emoji(":art:"),
                    is_(equal_to("🎨")))

    with it("translates :muscle:"):
        assert_that(sub_emoji(":muscle:"),
                    is_(equal_to("💪")))

    with it("translates :white_check_mark: (which has underscores)"):
        assert_that(sub_emoji(":white_check_mark:"),
                    is_(equal_to("✅")))

    with it("translates :star2: (which has a number)"):
        assert_that(sub_emoji(":star2:"),
                    is_(equal_to("🌟")))

    with it("translates :+1: (which has a +)"):
        assert_that(sub_emoji(":+1:"),
                    is_(equal_to("👍")))

    with it("translates :-1: (which has a -)"):
        assert_that(sub_emoji(":-1:"),
                    is_(equal_to("👎")))

    with it("can deal with multiple emojis and text"):
        assert_that(sub_emoji("both :art: and :muscle: at once"),
                    is_(equal_to("both 🎨 and 💪 at once")))
