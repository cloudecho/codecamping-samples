package main

import "fmt"

func main() {
	var sum = 0
	for i := 1; i <= 100; i++ {
		sum += i
	}
	fmt.Println("1+2+...+100 =", sum)

}
