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
from hamcrest import *
import unittest

from beam.estimates import Estimate

class NothingTest (unittest.TestCase):

    def test_properties_are_stored (self):
        e = Estimate(1, 2, 3)
        assert_that(e.best, is_(equal_to(1)))
        assert_that(e.expected, is_(equal_to(2)))
        assert_that(e.worst, is_(equal_to(3)))

    def test_different_properties_are_stored (self):
        e = Estimate(2, 4, 8)
        assert_that(e.best, is_(equal_to(2)))
        assert_that(e.expected, is_(equal_to(4)))
        assert_that(e.worst, is_(equal_to(8)))

    def test_best_case_cannot_be_worse_than_expected_case (self):
        assert_that(calling(Estimate).with_args(2, 1, 3),
                    raises(ValueError))

    def test_worst_case_cannot_be_better_than_expected_case (self):
        assert_that(calling(Estimate).with_args(1, 3, 2),
                    raises(ValueError))
