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
from re import compile as re_compile

cdef RE_NUMBER = re_compile(r"^[0-9]+(?:\.[0-9]+)*$")
cdef RE_DOUBLE_QUOTE_ESCAPES = re_compile(r'["$]')
cdef RE_RAW_ESCAPES = re_compile(r"[^-+%./=@\\_0-9A-Za-z]")

cdef escape_char (match):
    return "\\" + match.group(0)

cdef class ShellLiteral:

    cdef str value

    def __init__ (self, value):
        self.value = str(value)

    def raw (self):
        self.assert_we_can_generate_a_raw_literal()
        return self.escape(RE_RAW_ESCAPES)

    def __str__ (self):
        if self.single_quote_is_in_value():
            return self.double_quote()

        elif self.is_number():
            return self.value

        else:
            return self.single_quote()

    def __repr__ (self):
        return "<{} {}>".format(self.__class__.__name__, str(self))

    cdef assert_we_can_generate_a_raw_literal (self):
        if self.contains_linefeed():
            raise ValueError(
                    "cannot represent linefeeds in raw literals")

    cdef bint contains_linefeed (self):
        return "\n" in self.value

    cdef bint single_quote_is_in_value (self):
        return "'" in self.value

    cdef bint is_number (self):
        return RE_NUMBER.match(self.value)

    cdef str double_quote (self):
        return '"{}"'.format(self.escape(RE_DOUBLE_QUOTE_ESCAPES))

    cdef str single_quote (self):
        return "'{}'".format(self.value)

    cdef str escape (self, regex):
        cdef str result = self.value.replace("\\", "\\\\")
        return regex.sub(escape_char, result)
