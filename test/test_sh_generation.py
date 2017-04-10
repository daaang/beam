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

    def assert_str (self, init, expected_str):
        literal = ShellLiteral(init)
        assert_that(literal, has_string(expected_str))

    def test_empty_string_becomes_two_apostrophes (self):
        self.assert_str("", "''")

    def test_strings_of_text_are_put_between_apostrophes (self):
        self.assert_str("matt", "'matt'")

    def test_apostrophes_have_no_special_characters (self):
        self.assert_str('\\ "" $var',
                        """'\\ "" $var'""")

    def test_text_containing_apostrophes_needs_double_quotes (self):
        self.assert_str("li'l configure",
                        '"li\'l configure"')

    def test_double_quotes_do_have_special_characters (self):
        self.assert_str("""\\ " ' $var""",
                        '"\\\\ \\" \' \\$var"')

    def test_integers_default_to_raw (self):
        self.assert_str(4, "4")

        self.assert_str(81, "81")

    def test_floats_default_to_raw (self):
        self.assert_str("3.5", "3.5")

    def test_numbers_do_not_begin_with_dots (self):
        self.assert_str(".2", "'.2'")

    def test_numbers_do_not_end_with_dots (self):
        self.assert_str("1.", "'1.'")

    def test_floats_can_have_multiple_decimals (self):
        self.assert_str("123.456", "123.456")

    def test_floats_can_have_multiple_dots (self):
        self.assert_str("123.456.789", "123.456.789")

    def test_floats_cannot_have_multiple_dots_in_a_row (self):
        self.assert_str("123..789", "'123..789'")

    def test_shortcut_args_are_raw_by_default (self):
        self.assert_str("-t", "-t")
        self.assert_str("-auND", "-auND")

    def test_optional_args_are_raw_by_default (self):
        self.assert_str("--hey", "--hey")

    def test_equal_signs_can_be_in_optional_args (self):
        self.assert_str("--my-name=Matt", "--my-name=Matt")

    def test_tab_can_be_escaped (self):
        self.assert_str("\t", "'\t'")

        literal = ShellLiteral("\t")
        assert_that(literal.raw(), is_(equal_to("\\\t")))

    def test_newline_cannot_be_raw (self):
        self.assert_str("\n", "'\n'")

        literal = ShellLiteral("\n")
        assert_that(calling(literal.raw), raises(ValueError))

class GivenAllNonAlphaNum (unittest.TestCase):

    def setUp (self):
        self.literal = ShellLiteral(
                " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    def test_defaults_to_double_quotes (self):
        assert_that(self.literal, has_string(
                '" !\\"#\\$%&\'()*+,-./:;<=>?@[\\\\]^_`{|}~"'))

    def test_can_represent_without_quotes (self):
        raw = self.literal.raw()
        assert_that(raw, is_(equal_to("\\ \\!\\\"\\#\\$%\\&\\'\\(\\)"
                                      "\\*+\\,-./\\:\\;\\<=\\>\\?@\\["
                                      "\\\\\\]\\^_\\`\\{\\|\\}\\~")))

class GivenMyName (unittest.TestCase):

    def setUp (self):
        self.literal = ShellLiteral("Matt LaChance")

    def test_defaults_to_single_quotes (self):
        assert_that(self.literal, has_string("'Matt LaChance'"))
