package main

import "fmt"

func chanDemo() {
	// 如下定义channel，默认c==cil，如果c为nil则无法使用，因此channel应该使用make来定义
	//var c chan int
	c := make(chan int)
	go func() {
		for {
			// 从channel中获取写入的数据
			n := <- c
			fmt.Println(n)
		}
	}()
	// 向channel中发送两个数据
	c <- 13
	c <- 2


}

func main() {
	chanDemo()
}