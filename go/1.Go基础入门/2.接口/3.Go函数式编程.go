package main

import "fmt"

// 函数式编程

// 闭包：闭包的体现形式，能常就是用函数返回另一个函数
// 		闭包的实现确保只要闭包还被使用，那么被闭包引用的变量会一直存在。如sum
//		由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包

// func 函数名(参数列表) 返回函数 {}
func adder () func(int) int {
	// 自由变量
	sum := 0
	return func(i int) int {
		// i为局部变量
		sum += i
		return sum
	}
}


func main() {
	a := adder()
	for i:= 0; i<10; i++ {
		fmt.Println(a(i))
	}
}