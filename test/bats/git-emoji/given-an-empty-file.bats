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

source test/bats/git-emoji/includes.sh

setup() {
  filename="`mktemp XXXXXX.txt`"
}

teardown() {
  rm "$filename"
}

@test "git-emoji --ed-commit-msg appends to weird commit messages" {
  cat <<EOF > "$filename"
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
maybe some diff stuff here
EOF
  git_emoji --ed-commit-msg "$filename"
  run cat "$filename"
  pattern='# =* =* =* =*'
  [ "${lines[3]}" = "maybe some diff stuff here" ]
  [[ ${lines[5]} =~ $pattern ]]
}
