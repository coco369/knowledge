package main

import "fmt"

func PrintSlice(s []int) {
	// 打印s的值，s的长度，以及s的cap长度
	fmt.Printf("s=%v len=%d cap=%d\n", s, len(s), cap(s))
}


func main()  {
	var s [] int
	// 通过append往切片s中加入两个元素，分别为1和2
	s1 := append(s, 1)
	s2 := append(s1, 2)
	s3 := append(s2, 3)
	// 打印的结果为s=[1 2] len=2 cap=2
	PrintSlice(s3)
	fmt.Println(s3)

    // 实现切片
    s4 := s3[:1]
    fmt.Println(s4)
	s5 := append(s4, 5)
	// s4的结果为[1]
	fmt.Println(s4)
	// s5的结果为[1 5]，由于有cap的出现，因此结果出现这种情况，详情可以看11.2中的结论
	fmt.Println(s5)

	// 创建指定cap长度的slice
	// 使用make()方法创建指定长度和cap长度的slice
	s6 := make([]int, 10)
	s7 := make([]int, 10, 16)
	PrintSlice(s6)
	PrintSlice(s7)
	s8 := s7[:3]
	s9 := append(s8, 5)
	fmt.Println(s8)
	fmt.Println(s9)

	// copy拷贝, copy(s1, s2) 将s2中的值拷贝到s1中
	var s10 = []int{1,2,3}
	copy(s6, s10)
	// s10信息输出结果：s=[1 2 3] len=3 cap=3
	PrintSlice(s10)
	// s6信息输出结果：s=[1 2 3 0 0 0 0 0 0 0] len=10 cap=10
	PrintSlice(s6)

	// 删除，将s6中下标为2的元素删除掉
	// append(s6[:2], 元素)：表示向s6[:2]的结果中添加元素
	// 如果要合并两个slice，append(slice1，slice2...)，需要加三个点
	// 写法：append(s6[:2], s6[3:]...)
	s11 := append(s6[:2], s6[3:]...)
	// s11信息输出结果：s=[1 2 0 0 0 0 0 0 0] len=9 cap=10
	PrintSlice(s11)

}
