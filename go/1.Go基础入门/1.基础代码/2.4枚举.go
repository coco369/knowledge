package main

import "fmt"

// 枚举没有关键字来定义，一般使用const定义
// 普通枚举类型
// iota表示自增1
const (
	python = iota
	java
	cpp
	net
	javascript
)

// 定义执行的表达式
func menus () {
	// const中的每一个变量都将按照1<< 10 * iota这个表达式进行运算
	const (
		b = 1 << 10 * iota
		kb
		mb
		gb
		tb
		pb
	)
	fmt.Println(b, kb, mb, gb, tb, pb)

}

func main() {
	fmt.Println(python, java, cpp, net, javascript)

	menus()
}

