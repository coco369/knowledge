package main

import "fmt"

func main() {
	// 定义数组arr0，长度为3，且元素为int类型
	// 初始化数组中 {} 中的元素个数不能大于 [] 中的数字。
	var arr0 = [3]int{1, 2, 3}
	fmt.Println(arr0)

	// 如果忽略 [] 中的数字不设置数组大小，Go 语言会根据元素的个数来设置数组的大小：
	var arr1 = [...]float32{5, 3, 3.5}
	fmt.Println(arr1)
	// 通过下标大于数组内的元素，且下标不能越界
	fmt.Println(arr1[0], arr1[2])

	// 定义长度为3，且存储int类型的数组
	var arr2 [3]int
	for a := 0; a < 3; a++ {
		arr2[a] = a
	}
	fmt.Println(arr2)
}
