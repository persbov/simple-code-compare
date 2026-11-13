# Simple sum of a list of numbers in Mojo
# Algorithm is the same as in Python

fn main():
    var numbers = List[Int](1, 2, 3, 4, 5)
    var total: Int = 0

    for num in numbers:
        total += num[]

    print("Sum:", total)   # 15
