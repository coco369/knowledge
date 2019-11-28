package main

import (
	"fmt"
	"reflect"
)

// 常量使用const定义，表示const的数值可作为各种类型使用

const a = 1

const (
	b = "2"
	c = 4.0
)

func main()  {
	// 变量类型的打印，使用reflect.TypeOf(变量)
	fmt.Println(reflect.TypeOf(b))
	fmt.Println(reflect.TypeOf(c))
	fmt.Println(a, b, c)
}
