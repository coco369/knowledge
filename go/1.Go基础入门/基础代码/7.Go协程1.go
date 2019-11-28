package main

import "fmt"

func add(x, y int) {
	z := x + y
	fmt.Println(z)
}

func main() {
	for i := 0; i < 10; i++ {
		go add(i, i)
	}
}
