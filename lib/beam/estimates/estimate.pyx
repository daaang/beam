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

cdef class Estimate:

    cdef int best_case
    cdef int expected_case
    cdef int worst_case

    def __init__ (self, best, expected, worst):
        self.best_case = best
        self.expected_case = expected
        self.worst_case = worst

        self.assert_valid()

    @property
    def best (self):
        return self.best_case

    @property
    def expected (self):
        return self.expected_case

    @property
    def worst (self):
        return self.worst_case

    cdef assert_valid (self):
        if self.best_case > self.expected_case:
            raise ValueError("the best case must not be larger than"
                    " either other case")

        if self.worst_case < self.expected_case:
            raise ValueError("the worst case must not be smaller than"
                    " either other case")

        if self.best_case < 1:
            raise ValueError("all estimates must be greater than zero")
