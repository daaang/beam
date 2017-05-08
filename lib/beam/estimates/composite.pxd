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

from .estimate cimport Estimate

cdef class CompositeEstimate (Estimate):

    cdef inline int get_mean_times_six (self, estimate):
        return estimate.best + (4*estimate.expected) + estimate.worst

    cdef inline int ceiling_divide_by_six (self, int x):
        return (x + 5) // 6

    cdef int get_sum_of_means_times_six (self, estimates)
    cdef int get_sum_of_standard_deviations_times_six (self, estimates)
