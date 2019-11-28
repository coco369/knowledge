package main

import "fmt"

// 定义接收参数类型为数组的函数PrintArray

func PrintArray(arr [5]int) {
	for i, v := range arr {
		fmt.Println(i, v)
	}
}


func main () {

	var arr = [5]int{1,2,3,4,5}
	var a = 3
	PrintArray(arr)
	fmt.Println(a)
}