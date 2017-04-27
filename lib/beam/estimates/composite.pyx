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

cdef class CompositeEstimate:

    def __init__ (self, first_estimate, *args):
        cdef int means = self.get_mean_times_six(first_estimate)
        cdef int stddevs = first_estimate.worst - first_estimate.best
        cdef int expected = first_estimate.expected

        means += sum(self.get_mean_times_six(e) for e in args)
        stddevs += sum(e.worst - e.best for e in args)
        expected += sum(e.expected for e in args)

        if args:
            super().__init__(self.ceiling_divide_by_six(means - stddevs),
                             expected,
                             self.ceiling_divide_by_six(means + stddevs))

        else:
            super().__init__(first_estimate.best,
                             first_estimate.expected,
                             first_estimate.worst)
