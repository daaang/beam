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

git_emoji() {
  for lib in build/lib*; do
    PYTHONPATH="$lib" ./bin/git-emoji "$@"
  done
}

@test "git-emoji pipes plaintext stdin to stdout" {
  run git_emoji - <<EOF
Hi, Matt!
EOF
  [ "$status" = 0 ]
  [ "$output" = "Hi, Matt!" ]
}

@test "git-emoji matches emoji by name" {
  run git_emoji - <<EOF
Can deal with :muscle: and :white_check_mark: at least
EOF
  [ "$status" = 0 ]
  [ "$output" = "Can deal with 💪  and ✅  at least" ]
}
