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

from lilconf.shell_generation.shell_literal import ShellLiteral

class GivenNothing (unittest.TestCase):

    def assert_defaults_to (self, init, expected_str):
        literal = ShellLiteral(init)
        assert_that(literal, has_string(expected_str))

    def test_empty_string_becomes_two_apostrophes (self):
        self.assert_defaults_to("", "''")

    def test_strings_of_text_are_put_between_apostrophes (self):
        self.assert_defaults_to("matt", "'matt'")

    def test_apostrophes_have_no_special_characters (self):
        self.assert_defaults_to('\\ "" $var',
                                """'\\ "" $var'""")

    def test_text_containing_apostrophes_needs_double_quotes (self):
        self.assert_defaults_to("li'l configure",
                                '"li\'l configure"')

    def test_double_quotes_do_have_special_characters (self):
        self.assert_defaults_to("""\\ " ' $var""",
                                '"\\\\ \\" \' \\$var"')

    def test_integers_default_to_raw (self):
        self.assert_defaults_to(4, "4")

        self.assert_defaults_to(81, "81")

    def test_floats_default_to_raw (self):
        self.assert_defaults_to("3.5", "3.5")

    def test_numbers_do_not_begin_with_dots (self):
        self.assert_defaults_to(".2", "'.2'")

    def test_numbers_do_not_end_with_dots (self):
        self.assert_defaults_to("1.", "'1.'")

    def test_floats_can_have_multiple_decimals (self):
        self.assert_defaults_to("123.456", "123.456")

    def test_floats_can_have_multiple_dots (self):
        self.assert_defaults_to("123.456.789", "123.456.789")

    def test_floats_cannot_have_multiple_dots_in_a_row (self):
        self.assert_defaults_to("123..789", "'123..789'")

    def test_shortcut_args_are_raw_by_default (self):
        self.assert_defaults_to("-t", "-t")
        self.assert_defaults_to("-auND", "-auND")

    def test_optional_args_are_raw_by_default (self):
        self.assert_defaults_to("--hey", "--hey")

    def test_equal_signs_can_be_in_optional_args (self):
        self.assert_defaults_to("--my-name=Matt", "--my-name=Matt")

class ShellLiteralTestCase (unittest.TestCase):

    def setUp (self):
        self.literal = ShellLiteral(self.value)

    def get_arg_str (self):
        return self.literal.arg_str()

    def get_raw (self):
        return self.literal.raw()

    def get_single_quote (self):
        return self.literal.single_quote()

    def get_double_quote (self):
        return self.literal.double_quote()

    def assert_default_is (self, value):
        assert_that(self.literal, has_string(value))

    def assert_defaults_to_raw (self):
        self.assert_default_is(self.get_raw())

    def assert_defaults_to_single_quotes (self):
        self.assert_default_is(self.get_single_quote())

    def assert_defaults_to_double_quotes (self):
        self.assert_default_is(self.get_double_quote())

    def assert_raw_is (self, value):
        assert_that(self.get_raw(), is_(equal_to(value)))

    def assert_single_quote_is (self, value):
        assert_that(self.get_single_quote(), is_(equal_to(value)))

    def assert_double_quote_is (self, value):
        assert_that(self.get_double_quote(), is_(equal_to(value)))

class GivenHorizontalTab (ShellLiteralTestCase):

    value = "\t"

    def test_defaults_to_single_quotes (self):
        self.assert_defaults_to_single_quotes()

    def test_can_be_escaped_raw (self):
        self.assert_raw_is("\\\t")

class GivenLineFeed (ShellLiteralTestCase):

    value = "\n"

    def test_defaults_to_single_quotes (self):
        self.assert_defaults_to_single_quotes()

    def test_newline_cannot_be_raw (self):
        assert_that(calling(self.get_raw), raises(ValueError))

class GivenAllNonAlphaNum (ShellLiteralTestCase):

    value = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def test_defaults_to_double_quotes (self):
        self.assert_defaults_to_double_quotes()

    def test_double_quotes_escape_only_a_few_chars (self):
        self.assert_double_quote_is(
                '" !\\"#\\$%&\'()*+,-./:;<=>?@[\\\\]^_`{|}~"')

    def test_can_represent_without_quotes (self):
        self.assert_raw_is("\\ \\!\\\"\\#\\$%\\&\\'\\(\\)"
                           "\\*+\\,-./\\:\\;\\<=\\>\\?@\\["
                           "\\\\\\]\\^_\\`\\{\\|\\}\\~")

class GivenMyName (ShellLiteralTestCase):

    value = "Matt LaChance"

    def test_defaults_to_single_quotes (self):
        self.assert_defaults_to_single_quotes()

    def test_raw_escapes_the_space (self):
        self.assert_raw_is("Matt\\ LaChance")

    def test_can_specify_double_quotes (self):
        self.assert_double_quote_is('"Matt LaChance"')

    def test_can_specify_single_quotes (self):
        self.assert_single_quote_is("'Matt LaChance'")

    def test_arg_str_is_default (self):
        assert_that(self.get_arg_str(),
                    is_(equal_to("'Matt LaChance'")))

class GivenStrWithApostrophe (ShellLiteralTestCase):

    value = "Li'l Configure"

    def test_defaults_to_double_quotes (self):
        self.assert_defaults_to_double_quotes()

    def test_single_quotes_wrap_around_apostrophe (self):
        self.assert_single_quote_is("'Li'\\''l Configure'")

    def test_double_quotes_have_no_work_to_do (self):
        self.assert_double_quote_is('"Li\'l Configure"')

    def test_raw_escapes_quote_and_space (self):
        self.assert_raw_is("Li\\'l\\ Configure")
