package main

import "fmt"

// 交换两个变量的值

// 指针变量a与b，获取指针对应的值使用*a，*b
// 变量c与d，获取变量对应的指针使用&c，&d

func change(a, b *int) {
	*a, *b = *b, *a
}

func main () {
	a, b := 3, 4
	change(&a, &b)
	fmt.Println(a, b)
}