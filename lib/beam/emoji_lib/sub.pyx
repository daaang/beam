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
from re import compile as re_compile

from .duples import EMOJI_BY_NAME

cdef RE_EMOJI_NAME = re_compile(r":([-+_0-9a-z]+):")

cdef str emoji_repl (match):
    return EMOJI_BY_NAME.get(match.group(1), match.group(0))

cdef str spaced_emoji_repl (match):
    cdef str key = match.group(1)

    if key not in EMOJI_BY_NAME:
        return match.group(0)

    return EMOJI_BY_NAME[key] + " "

def sub_emoji (text):
    return RE_EMOJI_NAME.sub(emoji_repl, text)

def sub_emoji_term_io (text):
    return RE_EMOJI_NAME.sub(spaced_emoji_repl, text)
