package main

import "fmt"

// go只支持封装，不支持继承和多态
// go中没有class，只有结构struct

type Person struct {
	// 定义参数以及类型
	name string
	age int
}

func A (p Person) {
	p.age = 10
	fmt.Println(p)
}

func B (p *Person) {
	p.age = 10
	fmt.Println(p)
}

func main () {
	// 对struct的属性进行赋值操作，类似面向对象中类的使用
	a := Person{}
	a.name = "王海飞"
	a.age = 18
	fmt.Println(a)

	// 初始化值
	b := Person{
		name:"童蕊",
		age:18,
	}
	fmt.Println(b)

	// 将b变量传入A方法中
	A(b) // 在方法中将打印{童蕊 10}
	fmt.Println(b)  // 重新打印b变量，输出结果为{童蕊 18}
	// 注意以上的结果和向函数中传入数组类型的参数是一样的结果，因为参数传递时，采用值拷贝

	// 使用指针的形式，传入参数
	fmt.Println("使用指针的形式，传入参数")
	B(&b)  // 传入b变量的指针，方法B中修改指针对应的值，因此外部的b变量的值也将被修改
	fmt.Println(b)  // 输出打印的b变量的结果为{童蕊 10}

}
