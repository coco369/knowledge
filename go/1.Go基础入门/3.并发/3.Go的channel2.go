package main

import (
	"fmt"
	"time"
)

// 接收一个参数，参数类型为channel
func worker(c chan int) {
	for {
		// 从channel中获取写入的数据
		n := <- c
		fmt.Println(n)
	}
}

func chanDemo2() {
	// 如下定义channel，默认c==cil，如果c为nil则无法使用，因此channel应该使用make来定义
	//var c chan int
	c := make(chan int)
	go worker(c)
	// 向channel中发送两个数据
	c <- 4
	c <- 2

}

func chanDemo3() {
	c := make(chan int)
	go worker(c)
	c <- 'a'
	c <- 2
	c <- 3
	time.Sleep(time.Microsecond)

}

func main() {
	//chanDemo2()
	chanDemo3()
}