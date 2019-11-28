// 可执行的go程序必须引入package main
package main

import "fmt"

// 定义包内部的变量，不能使用:=
var s2 = 12

// 变量可以使用括号来定义变量
var (
	s3 = 14
	s4 = 43
)


// main函数入口点
func main() {
	var a int
	var b float32

	var c, d float64

	var s string

	fmt.Printf("%d %f %f %f %q", a, b, c, d, s)

	a = 5
	// = 使用必须使用先var声明例如
	c, d = 9, 10
	// := 是声明并赋值。并且系统自动推断类型，不需要var关键字
	var s1 = 13
	e, f := 11, 12

	fmt.Print(a, b, c, d, e, f)
	fmt.Println(s1)

}
