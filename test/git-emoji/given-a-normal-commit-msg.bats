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

source test/git-emoji/includes.sh

setup() {
  filename="`mktemp XXXXXX.txt`"
  cat <<EOF > "$filename"
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Changes to be committed:
#	[etc]
#
# ------------------------ >8 ------------------------
# Do not touch the line above.
# Everything below will be removed.
maybe some diff stuff here
EOF
  git_emoji --ed-commit-msg "$filename"
  status="$?"
}

teardown() {
  rm "$filename"
}

@test "git-emoji --ed-commit-msg succeeds" {
  [ "$status" = 0 ]
}

@test "git-emoji --ed-commit-msg doesn't change the last line" {
  [ "`tail -n 1 $filename`" = "maybe some diff stuff here" ]
}

@test "git-emoji --ed-commit-msg doesn't change the first ten lines" {
  run cat "$filename"
  [ "${lines[9]}" = "# Everything below will be removed." ]
}

@test "git-emoji --ed-commit-msg does add the table" {
  run cat "$filename"
  pattern='^# =* =* =* =*$'
  [[ ${lines[11]} =~ $pattern ]]
}
