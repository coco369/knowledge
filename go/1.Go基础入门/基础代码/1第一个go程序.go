// 必须在源文件中非注解的第一行知名这个文件属于哪个包。每一个Go程序都应该包含一个名为main包
// 表示可独立允许的程序
package main

// 告诉GO解释器这个程序必须使用fmt包，fmt包实现量格式化IO（输入/输出）的函数
import (
	"fmt"
)

// main()是程序的入口，main函数是每一个可执行程序所必须包含的。
func main() {
	// 打印输出字符串
	/* 多行注释 */
	fmt.Print("Hello World")
}
