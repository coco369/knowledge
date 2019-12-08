package main

import (
	"fmt"
	"runtime"
	"time"
)

func main()  {

	var a [10]int
	for i := 0; i < 10; i++ {
		go func(i int) {
			for {
				// 协程中一直对数组a中对元素进行加一操作，因此协程并没有主动退出
				// 协程没有交出控制权，则其他的goroutine并不能执行
				a[i]++
				// 以下代码为主动交出控制权，其他的goroutine才能执行
				runtime.Gosched()
			}
		}(i)
	}
	time.Sleep(time.Microsecond)
	// 最后打印a数组的值
	fmt.Println(a)
}
