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

from beam.estimates import Estimate, CompositeEstimate

class Mod: pass

with description("an Estimate object"):
    with context("inited with (1, 2, 3)"):
        with before.each:
            Mod.e = Estimate(1, 2, 3)

        with it("has a best case of 1"):
            assert_that(Mod.e.best, is_(equal_to(1)))

        with it("has an expected case of 2"):
            assert_that(Mod.e.expected, is_(equal_to(2)))

        with it("has a worst case of 3"):
            assert_that(Mod.e.worst, is_(equal_to(3)))

        with it("can be set as a triple"):
            a, b, c = Mod.e
            assert_that(a, is_(equal_to(1)))
            assert_that(b, is_(equal_to(2)))
            assert_that(c, is_(equal_to(3)))

    with context("inited with (2, 4, 8)"):
        with before.each:
            Mod.e = Estimate(2, 4, 8)

        with it("has a best case of 2"):
            assert_that(Mod.e.best, is_(equal_to(2)))

        with it("has an expected case of 4"):
            assert_that(Mod.e.expected, is_(equal_to(4)))

        with it("has a worst case of 8"):
            assert_that(Mod.e.worst, is_(equal_to(8)))

        with it("can be set as a triple"):
            a, b, c = Mod.e
            assert_that(a, is_(equal_to(2)))
            assert_that(b, is_(equal_to(4)))
            assert_that(c, is_(equal_to(8)))

    with it("doesn't allow a worst best case than its expected case"):
        assert_that(calling(Estimate).with_args(2, 1, 3),
                    raises(ValueError))

    with it("doesn't allow a better worst case than its expected case"):
        assert_that(calling(Estimate).with_args(1, 3, 2),
                    raises(ValueError))

    with it("does allow all cases to be equal"):
        e = Estimate(1, 1, 1) # no exception

    with it("doesn't allow any cases at zero or less"):
        assert_that(calling(Estimate).with_args(0, 1, 2),
                    raises(ValueError))

with description("a CompositeEstimate object"):
    with it("must have at least one child estimate"):
        assert_that(calling(CompositeEstimate).with_args(),
                    raises(TypeError))

    with context("an estimate of (1, 4, 9) exists"):
        with before.each:
            Mod.first = Estimate(1, 4, 9)

        with it("a one-item composite copies its only child"):
            assert_that(CompositeEstimate(Mod.first),
                        is_(equal_to(Mod.first)))

        with context("a second estimate of (2, 3, 5) exists"):
            with before.each:
                Mod.second = Estimate(2, 3, 5)

            with it("their composite is (6, 7, 10)"):
                assert_that(CompositeEstimate(Mod.first, Mod.second),
                            is_(equal_to(Estimate(6, 7, 10))))

            with context("a third estimate of (2, 3, 12) exists"):
                with before.each:
                    Mod.third = Estimate(2, 3, 12)
                    Mod.all_three = CompositeEstimate(Mod.first,
                                                      Mod.second,
                                                      Mod.third)

                with it("their composite is (6, 7, 10)"):
                    assert_that(Mod.all_three,
                                is_(equal_to(Estimate(9, 10, 16))))

                with it("can produce an identical nested composite"):
                    assert_that(CompositeEstimate(
                                    CompositeEstimate(Mod.first,
                                                      Mod.second),
                                    Mod.third),
                                is_(equal_to(Mod.all_three)))
