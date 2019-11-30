package main

import (
	"fmt"
	"time"
)

func product(p chan int) {
	for i := 0; i < 10; i++ {
		fmt.Println("send:", i)
		p <- i // 向channel中写入数据

	}
}

func consumer(c chan int) {
	for i := 0; i < 10; i++ {
		c := <-c // 从channel中读取入数据
		fmt.Println("receive:", c)
	}
}

func main() {
	ch := make(chan int, 10)
	go product(ch)          // 创建一个生产者协程
	go consumer(ch)         // 创建一个消费者协程
	time.Sleep(time.Second) // 等待足够长的时间，直到协程执行完毕主进程才结束
}
