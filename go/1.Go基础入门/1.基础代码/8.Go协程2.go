package main

import (
	"fmt"
	"sync"
)

func main() {

	wg := sync.WaitGroup{}
	//var wg sync.WaitGroup
	wg.Add(10)
	for i := 0; i < 10; i++ {
		//go Add1(i, i, wg)
		go func(i int, x int) {
			fmt.Println("执行add方法", i)
			z := i + i
			fmt.Println("执行add方法结束", i)
			fmt.Println(z)
			wg.Done()
		}(i, 1)

	}
	wg.Wait()

}
