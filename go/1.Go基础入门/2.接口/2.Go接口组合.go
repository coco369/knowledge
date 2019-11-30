package main

// 接口的组合定义
// 总结：使用interface定义的接口，里面可以定义方法，该方法可以不用实现
//		而且interface接口中还可以定义其他的interface接口
//		而方法的实现则在结构体struct中定义


import (
	"fmt"
	"he/interface_combination"
)

// 定义接口
type A1 interface {
	Get(url string) string
}

type B1 interface {
	Div(a int, b int) int
}

type C1 interface {
	Print(msg string) string
}

// 定义组合接口
type D1 interface {
	A1
	B1
	C1
}


func f (d D1) {
	fmt.Println(d.Get("http://www.baidu.com"))
	fmt.Println(d.Div(10, 4))
	fmt.Println(d.Print("hello world"))
}

func main() {
	var r D1
	r = interface_combination.A{}
	f(r)
}


