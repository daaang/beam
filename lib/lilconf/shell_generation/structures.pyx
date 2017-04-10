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

cdef class ShellAssignment:

    cdef str name
    cdef str value

    def __init__ (self, name, value):
        self.name = name
        self.value = value

    def __str__ (self):
        return "=".join((self.name, self.value))

cdef class ShellSequence:

    cdef str line

    def __init__ (self, line):
        self.line = line

    def __str__ (self):
        return self.line
