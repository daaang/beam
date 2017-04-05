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

cdef class RstTable:

    cdef tuple c_header
    cdef int column_count
    cdef str c_str

    def __init__ (self, spec):
        del self.header
        self.c_str = ""
        self.column_count = len(spec)

    @property
    def header (self):
        return self.c_header

    @header.deleter
    def header (self):
        self.c_header = None

    def add_header (self, *fields):
        if len(fields) == self.column_count:
            self.c_header = fields

        else:
            raise TypeError

    def add_data (self, value):
        pass

    def __len__ (self):
        return 0

    def __iter__ (self):
        return iter(())

    def __str__ (self):
        return self.c_str

    def __repr__ (self):
        return "<{}>".format(self.__class__.__name__)
