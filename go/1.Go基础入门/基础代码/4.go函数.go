package main

import "fmt"

// 参数定义时，一定要定义参数的类型。如果有返回值也要定义返回值的类型
// 返回一个参数
func sum(a float32, b float32) float32 {
	return a + b
}

// 返回两个参数(没有定义参数名)
func div(a, b int) (int, int) {
	return a/b, a%b
}

// 返回两个参数（指定了参数名）
func div1(a int, b int) (q, r int) {
	q = a / b
	r = a % b
	return q, r
}




func main() {
	fmt.Println("the result is :", sum(2.2, 2.9))

	fmt.Println(div(13, 3))

	fmt.Println(div1(15, 4))
}

// 2.2+2.9的结果为5.1000004，是存在误差的
