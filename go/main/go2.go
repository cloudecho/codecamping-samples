package main

import "fmt"

func main() {
	var sum = accumulate(1, 100)
	fmt.Println("1+2+...+100 =", sum)

	fmt.Println("5! =", factorial(5))
}

func accumulate(start int, end int) int {
	if end == start {
		return start
	}
	return end + accumulate(start, end-1)
}


func factorial( n int) int {
	if n == 0 {
		return 1
	} else {
		return n * factorial(n - 1)
	}
}
