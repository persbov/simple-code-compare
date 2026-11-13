// Simple sum of a list of numbers in Dart
// Algorithm: go through each number and add it to a running total

void main() {
  var numbers = [1, 2, 3, 4, 5];
  var total = 0;

  for (var num in numbers) {
    total += num;
  }

  print('Sum: $total'); // 15
}
