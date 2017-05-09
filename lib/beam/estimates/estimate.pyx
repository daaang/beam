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

    def __init__ (self, best, expected, worst):
        self.best_case = best
        self.expected_case = expected
        self.worst_case = worst

        self.validate_our_estimates()

    @property
    def best (self):
        return self.best_case

    @property
    def expected (self):
        return self.expected_case

    @property
    def worst (self):
        return self.worst_case

    def get_mean_times_six (self):
        return 4*self.expected + self.best + self.worst

    def __iter__ (self):
        yield self.best
        yield self.expected
        yield self.worst

    def __richcmp__ (self, rhs, comparison_id):
        if comparison_id == 2:
            return self.best == rhs.best \
               and self.expected == rhs.expected \
               and self.worst == rhs.worst

        elif comparison_id == 3:
            return self.best != rhs.best \
                or self.expected != rhs.expected \
                or self.worst != rhs.worst

        else:
            self_avg = 4*self.expected + self.best + self.worst
            rhs_avg = 4*rhs.expected + rhs.best + rhs.worst

            if comparison_id == 0:
                return self_avg < rhs_avg

            elif comparison_id == 1:
                return self_avg <= rhs_avg

            elif comparison_id == 4:
                return self_avg > rhs_avg

            elif comparison_id == 5:
                return self_avg >= rhs_avg

            else:
                raise ValueError("Unexpected compare: {:d}".format(
                                comparison_id))

    def __repr__ (self):
        return "<{} {:d} {:d} {:d}>".format(
                self.__class__.__name__,
                self.best,
                self.expected,
                self.worst)

    cdef validate_our_estimates (self):
        self.assert_best_case_is_best()
        self.assert_worst_case_is_worst()
        self.assert_all_estimates_are_positive()
