package main

import "fmt"

// 交换两个变量的值

// 指针变量a与b，获取指针对应的值使用*a，*b
// 变量c与d，获取变量对应的指针使用&c，&d

func change(a, b *int) {
	*a, *b = *b, *a
}

func change2(a, b int) (int, int) {
	return b, a
}

func main () {
	// 交换两个值，使用指针，方法1
	a, b := 3, 4
	change(&a, &b)
	fmt.Println(a, b)

	// 交换两个值，不实用指针，方法2
	c, d := 3, 4
	c, d = change2(c, d)
	fmt.Println(c, d)
}