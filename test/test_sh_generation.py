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

from lilconf.sh_gen import ShellLiteral

class TestShellLiteral (unittest.TestCase):

    def test_empty_string_becomes_two_apostrophes (self):
        literal = ShellLiteral("")
        assert_that(literal, has_string("''"))

    def test_strings_of_text_are_put_between_apostrophes (self):
        literal = ShellLiteral("matt")
        assert_that(literal, has_string("'matt'"))

    def test_apostrophes_have_no_special_characters (self):
        literal = ShellLiteral('\\ "" $var')
        assert_that(literal, has_string("""'\\ "" $var'"""))

    def test_text_containing_apostrophes_needs_double_quotes (self):
        literal = ShellLiteral("li'l configure")
        assert_that(literal, has_string('"li\'l configure"'))

    def test_double_quotes_do_have_special_characters (self):
        literal = ShellLiteral("""\\ " ' $var""")
        assert_that(literal, has_string('"\\\\ \\" \' \\$var"'))
