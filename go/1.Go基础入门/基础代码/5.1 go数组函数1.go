package main

import "fmt"

// 定义接收参数类型为数组的函数PrintArray

func PrintArray2(arr [5]int) {
	// 改变数组arr中的第一值，修改为100
	arr[0] = 100
	for i, v := range arr {
		fmt.Println(i, v)
	}
}


func main () {

	var arr = [5]int{1,2,3,4,5}
	// 将arr传入进函数，在函数内修改arr中第一个参数，修改参数内的值并不会影响外面的arr参数
	PrintArray2(arr)
	// 打印外面的arr参数，其值没有被修改
	fmt.Println(arr)
}

//结论：参数传入函数内以后，函数内的修改并不影响外部的参数本身。因为数组是值拷贝。
//类似于python中的可变变量