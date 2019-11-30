package main

import (
	"fmt"
	"hello/api"
	"net/http"
)

// 封装
// 首字母大写：public
// 首字母小写：private

// 包
// main包包含可执行入口

func main () {

	fmt.Println(api.HelloWorld())
	fmt.Println(http.Cookie{})
}

