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
from collections import deque

cdef class RstTable:

    cdef tuple c_header
    cdef int column_count
    cdef int width
    cdef object data

    def __init__ (self, spec):
        del self.header
        self.data = deque()
        self.column_count = len(spec)
        self.width = 0

    @property
    def header (self):
        return self.c_header

    @header.deleter
    def header (self):
        self.c_header = None

    def add_header (self, *fields):
        if len(fields) == self.column_count:
            self.c_header = fields
            self.assert_width_at_least(fields[0])

        else:
            raise TypeError

    def add_data (self, *fields):
        self.data.append(fields[0])
        self.assert_width_at_least(fields[0])

    def __len__ (self):
        return 0

    def __iter__ (self):
        return iter(())

    def __str__ (self):
        if self.data:
            return self.generate_str()

        else:
            return ""

    def __repr__ (self):
        return "<{}>".format(self.__class__.__name__)

    cdef void assert_width_at_least (self, str s):
        cdef int w = len(s)

        if w > self.width:
            self.width = w+1 if self.is_even(w) else w

    cdef bint is_even (self, int x):
        return x % 2 == 0

    cdef str generate_str (self):
        if self.header is None:
            return self.get_data_str()

        else:
            return "{}\n{}".format(self.get_header_str(),
                                   self.get_data_str())

    cdef str get_header_str (self):
        return "{{}}\n{{:^{:d}}}" \
                .format(self.width) \
                .format(self.get_rule(), self.header[0]) \
                .rstrip(" ")

    cdef str get_data_str (self):
        return "{rule}\n{data}\n{rule}".format(
                rule=self.get_rule(),
                data="\n".join(self.data))

    cdef str get_rule (self):
        return "=" * self.width
