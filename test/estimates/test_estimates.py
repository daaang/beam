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

from beam.estimates import Estimate, CompositeEstimate

class GivenNothing (unittest.TestCase):

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

    def test_all_cases_can_be_equal (self):
        e = Estimate(1, 1, 1) # no exception

    def test_all_cases_must_be_greater_than_zero (self):
        assert_that(calling(Estimate).with_args(0, 1, 2),
                    raises(ValueError))

class GivenOneEstimate (unittest.TestCase):

    def setUp (self):
        self.first = Estimate(1, 4, 9)

class GivenTwoEstimates (GivenOneEstimate):

    def setUp (self):
        super().setUp()
        self.second = Estimate(2, 3, 5)

class TestOneEstimate (GivenOneEstimate):

    def test_can_set_as_triple (self):
        a, b, c = self.first
        assert_that(a, is_(equal_to(1)))
        assert_that(b, is_(equal_to(4)))
        assert_that(c, is_(equal_to(9)))

class TestTwoEstimates (GivenTwoEstimates):

    def test_can_set_as_triple (self):
        a, b, c = self.second
        assert_that(a, is_(equal_to(2)))
        assert_that(b, is_(equal_to(3)))
        assert_that(c, is_(equal_to(5)))

    def test_can_become_composite (self):
        c = CompositeEstimate(self.first, self.second)
        assert_that(list(c), is_(equal_to([6, 7, 10])))
