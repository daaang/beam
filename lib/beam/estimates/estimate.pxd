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

    cdef validate_our_estimates (self)

    cdef inline assert_best_case_is_best (self):
        if self.best_case > self.expected_case:
            raise ValueError("the best case must not be larger than"
                    " either other case")

    cdef inline assert_worst_case_is_worst (self):
        if self.worst_case < self.expected_case:
            raise ValueError("the worst case must not be smaller than"
                    " either other case")

    cdef inline assert_all_estimates_are_positive (self):
        if self.best_case < 1:
            raise ValueError("all estimates must be greater than zero")
