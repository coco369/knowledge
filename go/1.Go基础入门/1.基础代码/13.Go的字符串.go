package main

import (
	"fmt"
	"unicode/utf8"
)

// 注意：go中的len和python中的len都是打印字符串所占的字节数

func main () {
	// 采用utf-8编码，中文占3个字节，英文占1字节
	s := "hello哈哈 王海飞"
	// 使用len(变量)将打印变量所占的字节数，结果s的字节数为11
	fmt.Println(len(s))

	// 如果打印字符的数量, 使用RuneCountInString方法
	fmt.Println(utf8.RuneCountInString(s))

	// 获取s中的元素"王"，方法为以下两种
	fmt.Println(s[12:15])
	// rune相当于go的char
	fmt.Printf("%c ",[]rune(s)[8])
}
