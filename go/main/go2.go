package main

import "fmt"

func main() {
	var sum = accumulate(1, 100)
	fmt.Println("1+2+...+100 =", sum)
}

func accumulate(start int, end int) int {
	if end == start {
		return start
	}
	return end + accumulate(start, end-1)
}
