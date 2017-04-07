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

cdef RE_NUMBER = re_compile(r"^[0-9]+$")
cdef DOUBLE_QUOTE_ESCAPES = ('"', "$")
cdef ALL_ESCAPES = (
    "\\",
    "\t",
    " ",
    "!",
    '"',
    "#",
    "$",
    #"%",
    "&",
    "'",
    "(",
    ")",
    "*",
    #"+",
    ",",
    #"-",
    #".",
    #"/",
    ":",
    ";",
    "<",
    #"=",
    ">",
    "?",
    #"@",
    "[",
    "]",
    "^",
    #"_",
    "`",
    "{",
    "|",
    "}",
    "~",
)

cdef class ShellLiteral:

    cdef str value

    def __init__ (self, value):
        self.value = str(value)

    def raw (self):
        cdef str result = self.value

        for c in ALL_ESCAPES:
            result = result.replace(c, "\\" + c)

        return result

    def __str__ (self):
        if self.single_quote_is_in_value():
            return self.double_quote()

        elif self.is_number():
            return self.value

        else:
            return self.single_quote()

    def __repr__ (self):
        return "<{} {}>".format(self.__class__.__name__, str(self))

    cdef bint single_quote_is_in_value (self):
        return "'" in self.value

    cdef bint is_number (self):
        return RE_NUMBER.match(self.value)

    cdef str double_quote (self):
        cdef str result = self.value.replace("\\", "\\\\")

        for c in DOUBLE_QUOTE_ESCAPES:
            result = result.replace(c, "\\" + c)

        return '"{}"'.format(result)

    cdef str single_quote (self):
        return "'{}'".format(self.value)
