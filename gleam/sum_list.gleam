// Simple sum of a list of numbers in Gleam
// Algorithm: go through each number and add it to a running total

import gleam/io
import gleam/int
import gleam/list

pub fn main() {
  let numbers = [1, 2, 3, 4, 5]
  let total = list.fold(numbers, 0, fn(acc, num) { acc + num })

  io.println("Sum: " <> int.to_string(total)) // 15
}
