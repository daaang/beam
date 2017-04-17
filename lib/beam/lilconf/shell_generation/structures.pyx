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

cdef class BaseStructure:

    cdef str indent_str
    cdef str tab_str

    def __init__ (self):
        self.indent_str = ""
        self.tab_str = "  "

    @property
    def indent (self):
        return self.indent_str

    @indent.setter
    def indent (self, indent):
        self.indent_str = indent

    @property
    def tab (self):
        return self.tab_str

    @tab.setter
    def tab (self, tab):
        self.tab_str = tab

    def __str__ (self):
        return ""

    def __bool__ (self):
        return False

    def __repr__ (self):
        return "<{} {}>".format(self.__class__.__name__,
                                repr(str(self)))
