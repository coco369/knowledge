package main

import "fmt"

// 函数嵌套的定义
// func 函数名1（函数名2 func(参数) 返回类型, 函数1接收参数）函数1返回类型 {
//
// }

func f3 (f2 func(int, int) int, a, b int) int {
	fmt.Println(f2(a, b))
	return f2(a, b)
}

func ff (a, b int) int {
	return a + b
}

func main() {

	f3(ff,2, 4)
}
