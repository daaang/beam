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
from re import compile as re_compile, MULTILINE

from .duples import EMOJI_BY_CHAR
from ..rst_table import RstTable

cdef GIT_EMOJI_KEY = (
    ("⚡️", "init",          "Initial commit"),
    ("✅", "add",           "Add feature/test"),
    ("🚧", "skip",          "Add failing (skipped) test"),
    ("🎨", "refactor",      "Refactor tests"),
    ("💪", "flex",          'Refactor (or "flex") code'),
    ("📚", "data",          "Add data (i.e. without tests)"),
    ("💚", "ci",            "Mess with continuous integration"),
    ("🏠", "git-repo",      "Mess with repository structure"),
    ("📝", "Documentation", "Write documentation"),
)

cdef RE_START_OF_LINE = re_compile(r"^", MULTILINE)

def get_rst_table():
    table = RstTable("<<<")
    table.add_header("Character", "Name", "Use")
    table.force_width(0, 2)

    for emoji, keyword, description in GIT_EMOJI_KEY:
        table.add_data(emoji,
                       "``:{}:``".format(EMOJI_BY_CHAR[emoji]),
                       description)

    return str(table)

def get_commit_table():
    table = RstTable("><<<")
    table.force_width(0, 2)

    for emoji, keyword, description in GIT_EMOJI_KEY:
        arg = "-" + keyword[0]
        name = ":{}:".format(EMOJI_BY_CHAR[emoji])

        table.add_data(emoji, arg, name, description)

    return RE_START_OF_LINE.sub("# ", str(table))

def add_emoji_commit_args (parser):
    group = parser.add_argument_group("emoji category")
    group = group.add_mutually_exclusive_group()

    for emoji, keyword, description in GIT_EMOJI_KEY:
        short_arg = "-" + keyword[0]
        long_arg = "--" + keyword.lower()
        name = ":{}:".format(EMOJI_BY_CHAR[emoji])

        group.add_argument(short_arg,
                           long_arg,
                           action="store_const",
                           const=name,
                           dest="emoji_category",
                           default="",
                           help=description)
