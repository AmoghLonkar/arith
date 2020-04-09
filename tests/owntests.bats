load harness

@test "own-1" {
  check '10 + 11 * 12' '142'
}

@test "own-2" {
  check '2 + 2 - 1' '3'
}

@test "own-3" {
  check '-3 * 4 + -6 - -5' '-13'
}

@test "own-4" {
  check '21 - 8 + 11' '24'
}

@test "own-5" {
  check '5  * 26 - 12 + 13' '131'
}

