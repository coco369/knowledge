package main

import "fmt"

func main () {
	var arr = []int{0,1,2,3,4,5,6,7}
	fmt.Println(arr)

	s1 := append(arr, 8)
	fmt.Println(s1)
	// 打印的arr还是[0 1 2 3 4 5 6 7],s1变化为[0 1 2 3 4 5 6 7 8]
	fmt.Println(arr)

	fmt.Println("切片数据的处理")
	// s2的结果为[4,5,6]
	// 由于arr的长度为8，因此s2切片后虽然元素只有4,5,6,但是元素7还是可以通过range查询到
	s2 := arr[4:7]
	fmt.Println(s2)
	// s3的结果为[4,5,6,8]
	// 如果重新给s2添加新的值，那么s3的元素就多了一个，而arr数组相当于把元素7的值给替换掉
	// arr的长度最长只有8个元素，因此不能再加入新的元素了
	s3 := append(s2, 8)
	fmt.Println(s3)
	fmt.Println(s2)
	// arr的值[0 1 2 3 4 5 6 8]
	fmt.Println(arr)
}

