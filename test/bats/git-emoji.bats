@test "Can run git-emoji -h" {
  run ./bin/git-emoji -h
  [ "$status" = 0 ]
}
