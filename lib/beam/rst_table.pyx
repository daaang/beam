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
    cdef object data
    cdef list widths

    def __init__ (self, spec):
        del self.header
        self.data = deque()
        self.column_count = len(spec)
        self.widths = [0] * self.column_count

    @property
    def header (self):
        return self.c_header

    @header.deleter
    def header (self):
        self.c_header = None

    def add_header (self, *fields):
        if len(fields) == self.column_count:
            self.c_header = fields
            self.assert_width_at_least(fields)

        else:
            raise TypeError

    def add_data (self, *fields):
        self.data.append(fields)
        self.assert_width_at_least(fields)

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

    cdef void assert_width_at_least (self, tuple t):
        cdef int i, w

        for i in range(self.column_count):
            w = len(t[i])

            if w > self.widths[i]:
                self.widths[i] = w+1 if self.is_even(w) else w

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
                .format(self.widths[0]) \
                .format(self.get_rule(), self.header[0]) \
                .rstrip(" ")

    cdef str get_data_str (self):
        return "{rule}\n{data}\n{rule}".format(
                rule=self.get_rule(),
                data="\n".join(self.generate_row(r) for r in self.data))

    cdef str generate_row (self, tuple row):
        return " ".join(row)

    cdef str get_rule (self):
        return " ".join("=" * w for w in self.widths)
