package main

import "fmt"

//if/else的使用
// if判断条件不需要加括号
func f1() {

	a := 10
	b := 11
	if a > b{
		fmt.Println("a大于b")
	} else {
		fmt.Print("b大于a")
	}
}

// for循环的使用
// go 里面没有while关键字，可以用for+break实现
func main() {
	//标准for循环，注意表达式不带花括号
	for a := 0; a < 10; a++ {
		fmt.Println(a)
	}
	b := 0
	//无限循环，后不跟表达式
	//for true{
	for {
		fmt.Println(b)
		b++
		if b >= 10 {
			//break默认跳出本次循环，就近原则
			break
		}
	}
}
