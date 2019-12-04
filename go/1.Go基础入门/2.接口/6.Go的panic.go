package main

import "fmt"

// panic的使用
// 1. 停止当前函数执行
// 2. 一直向上返回，执行每一层的defer
// 3. 如果没有遇到recover，程序退出

// recover的使用
// 1. 仅在defer调用中使用
// 2. 获取panic的值，如panic("recover可以获取到的值")
// 3. 如果无法处理，可重新panic


//func tryPanic() {
//	// 程序将直接抛出错误，不再执行panic后的代码
//	panic(error.New("这是一个错误"))
//	fmt.Println("这句话将不再执行")
//}

func tryRecover() {
	// 使用recover接收panic中传递的错误信息，且recover只能在defer中定义
	defer func() {
		r := recover()  // 获取recover变量，用于获取panic中的错误
		if r != nil {
			fmt.Println(r, "抛出的错误为panic中的错误信息")
		}
		fmt.Println("b")
	}()
	fmt.Println("测试以下代码是否执行1")
	panic("异常信息处理")
	fmt.Println("测试以上代码是否执行2")  // 这里开始的代码将不再执行
}

func main() {
	//tryPanic()

	fmt.Println("a")
	tryRecover()
	fmt.Println("c")

}
