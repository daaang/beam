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
        self.sub_estimates = (first_estimate,) + args

        if args:
            self.init_with_many_estimates()

        else:
            super().__init__(first_estimate.best,
                             first_estimate.expected,
                             first_estimate.worst)

    @property
    def expected (self):
        return sum(x.expected for x in self.sub_estimates)

    def init_with_many_estimates (self):
        cdef int means = self.get_sum_of_means_times_six()
        cdef int stddevs = self.get_sum_of_standard_deviations_times_six()

        super().__init__(self.ceiling_divide_by_six(means - stddevs),
                         self.ceiling_divide_by_six(means),
                         self.ceiling_divide_by_six(means + stddevs))

    cdef int get_sum_of_means_times_six (self):
        return sum(self.get_mean_times_six(x) for x in self.sub_estimates)

    cdef int get_sum_of_standard_deviations_times_six (self):
        return sum(x.worst - x.best for x in self.sub_estimates)
