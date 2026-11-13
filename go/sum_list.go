package main

import "fmt"

// Simple sum of a list of numbers
// Algorithm: go through each number and add it to a running total

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	total := 0

	for _, num := range numbers {
		total += num
	}

	fmt.Println("Sum:", total) // 15
}
