package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// defer调用，确保在函数结束时发生
// 常用的场景有: open/close文件、Lock/Unlock、PrintHeader/printFooter

func tryDefer () {
	fmt.Println(1)
	fmt.Println(2)
}

func tryDefer2 () {
	// 在输出打印之前加来defer表示，在函数执行完以后才执行的输出打印语句
	defer fmt.Println(1)
	fmt.Println(2)
}

func tryDefer3() {
	// 先defer的内容后执行，最后defer的内容先执行。"先进后出 后入先出"
	defer fmt.Println(1)
	defer fmt.Println(2)
	fmt.Println(3)
}

func writeFile (filename string) {
	// 先新创建一个文件
	file, err := os.Create(filename)
	if err != nil {
		// 1. 使用panic进行错误的抛出，但是程序会中断
		//panic(err)
		// 2. 另外一种错误处理
		fmt.Printf("Error:%s", err)
		return
	}
	// 最后关掉文件
	defer file.Close()

	writer := bufio.NewWriter(file)
	// 关闭文件之前先将缓存中的文件提交到需要写入的文件中
	defer writer.Flush()

	for i := 1; i < 20; i++ {
		fmt.Println(strconv.Itoa(i))
		// int转化为string string := strconv.Itoa(int)
		// string转化为int，int, err := strconv.Atoi(string)
		fmt.Fprintln(writer, strconv.Itoa(i))
	}
}


func main() {
	// tryDefer()结果的打印为1  2
	tryDefer()
	// tryDefer2()结果的打印为2  1
	tryDefer2()
	// tryDefer3()结果的打印为3  2  1
	tryDefer3()

	writeFile("abc.txt")
}
