package main

import "fmt"

// 定义结构体
type Student struct {
	Name    string
	Age     int
	Address Addr
}

type Addr struct {
	City string
}

func main() {

	// 定义channel
	stuchannel := make(chan Student, 8)

	// 向channel中写入数据
	stu := Student{"王海飞", 18, Addr{"成都"}}
	stuchannel <- stu

	// 修改stu中的信息
	stu.Age = 19

	// 取出channel中的数据
	stu_info := <-stuchannel
	fmt.Println("stu_info信息为：", stu_info)

}
