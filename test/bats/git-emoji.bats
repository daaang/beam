git_emoji() {
  for lib in build/lib*; do
    PYTHONPATH="$lib" ./bin/git-emoji "$@"
  done
}

@test "Can run git-emoji -h" {
  run git_emoji -h
  [ "$status" = 0 ]
}
