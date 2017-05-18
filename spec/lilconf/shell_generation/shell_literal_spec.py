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

from beam.lilconf.shell_generation.shell_literal import ShellLiteral

def assert_defaults_to (init_value, expected_str):
    literal = ShellLiteral(init_value)
    assert_that(str(literal), is_(equal_to(expected_str)))

with describe("default ShellLiteral str values"):
    with it("shows an empty str as two apostrophes"):
        assert_defaults_to("", "''")

    with it("wraps strings of text in apostrophes"):
        assert_defaults_to("matt", "'matt'")

    with it("escapes nothing when using apostrophes"):
        assert_defaults_to('\\ "" $var',
                           "'\\ \"\" $var'")

    with it("uses double quotes when apostrophes appear"):
        assert_defaults_to("li'l configure",
                           '"li\'l configure"')

    with it("escapes \\, \", and $ inside double quotes"):
        assert_defaults_to("""\\ " ' $var""",
                           '"\\\\ \\" \' \\$var"')

    with it("doesn't wrap integers in anything"):
        assert_defaults_to(4, "4")
        assert_defaults_to(81, "81")

    with it("doesn't wrap floats either"):
        assert_defaults_to("3.5", "3.5")

    with it("wraps numbers beginning with dots"):
        assert_defaults_to(".2", "'.2'")

    with it("wraps numbers ending with dots"):
        assert_defaults_to("1.", "'1.'")

    with it("leaves multi-decimal floats alone"):
        assert_defaults_to("123.456", "123.456")

    with it("treats multi-dot decimals as floats"):
        assert_defaults_to("123.456.789", "123.456.789")

    with it("treats two dots in a row as \"not a float\""):
        assert_defaults_to("123..789", "'123..789'")

    with it("leaves shortcut args as they come"):
        assert_defaults_to("-t", "-t")
        assert_defaults_to("-auND", "-auND")

    with it("leaves optional args alone"):
        assert_defaults_to("--hey", "--hey")

    with it("ignores equal signs in long args"):
        assert_defaults_to("--my-name=Matt", "--my-name=Matt")

with describe("a shell literal with '\\t'"):
    with before.each:
        self.literal = ShellLiteral("\t")

    with it("defaults to single quotes"):
        assert_that(str(self.literal), is_(equal_to("'\t'")))

    with it("can be escaped as a raw string"):
        assert_that(self.literal.raw(), is_(equal_to("\\\t")))

with describe("a shell literal with '\\n'"):
    with before.each:
        self.literal = ShellLiteral("\n")

    with it("defaults to single quotes"):
        assert_that(str(self.literal), is_(equal_to("'\n'")))

    with it("can't be escaped as a raw string"):
        assert_that(calling(self.literal.raw), raises(ValueError))

with describe("a shell literal with every non-alphanumeric ascii char"):
    with before.each:
        self.literal = ShellLiteral(
                " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    with it("defaults to double quotes"):
        assert_that(str(self.literal),
                    is_(equal_to(self.literal.double_quote())))

    with it("double quotes escape only a few chars"):
        assert_that(self.literal.double_quote(), is_(equal_to(
                '" !\\"#\\$%&\'()*+,-./:;<=>?@[\\\\]^_`{|}~"')))

    with it("can be represented without quotes"):
        assert_that(self.literal.raw(), is_(equal_to(
                            "\\ \\!\\\"\\#\\$%\\&\\'\\(\\)"
                            "\\*+\\,-./\\:\\;\\<=\\>\\?@\\["
                            "\\\\\\]\\^_\\`\\{\\|\\}\\~")))

with describe("a shell literal with 'Matt LaChance'"):
    with before.each:
        self.literal = ShellLiteral("Matt LaChance")

    with it("defaults to single quotes"):
        assert_that(str(self.literal),
                    is_(equal_to("'Matt LaChance'")))

    with it("escapes the space in its raw form"):
        assert_that(self.literal.raw(),
                    is_(equal_to("Matt\\ LaChance")))

    with it("can specify single quotes"):
        assert_that(self.literal.single_quote(),
                    is_(equal_to("'Matt LaChance'")))

    with it("can specify double quotes"):
        assert_that(self.literal.double_quote(),
                    is_(equal_to('"Matt LaChance"')))

    with it("single-quotes its arg str"):
        assert_that(self.literal.arg_str(),
                    is_(equal_to("'Matt LaChance'")))

    with it("single-quotes its value str"):
        assert_that(self.literal.value_str(),
                    is_(equal_to("'Matt LaChance'")))

with describe("a shell literal with \"Li'l Configure\""):
    with before.each:
        self.literal = ShellLiteral("Li'l Configure")

    with it("defaults to double quotes"):
        assert_that(str(self.literal),
                    is_(equal_to('"Li\'l Configure"')))

    with it("can wrap around the apostrophe with single quotes"):
        assert_that(self.literal.single_quote(),
                    is_(equal_to("'Li'\\''l Configure'")))

    with it("can easily wrap in double quotes"):
        assert_that(self.literal.double_quote(),
                    is_(equal_to('"Li\'l Configure"')))

    with it("can escape apostrophe and space when raw"):
        assert_that(self.literal.raw(),
                    is_(equal_to("Li\\'l\\ Configure")))
