package main

import (
	"fmt"
	"he/baidu"
)

// interface(接口)概念以及接口的定义
// interface类型可以定义一组方法，但这些方法可以不用实现。也可以不用定义任何的方法
// type 接口名称 interface {
// 		方法名（参数列表）返回值列表
// }

type Retriever interface {
	// 使用interface定义函数，函数不用加func关键字
	Get(url string) string
}

//// 定义结构体
//type A struct {
//	UserAgent string
//}
//
//// 定义结构体A实现的Get方法
//func (a A) Get(url string) string {
//	//res, err := http.Get(url)
//	//if err != nil{
//	//	panic(err)
//	//}
//	//
//	//result, err := httputil.DumpResponse(res, true)
//	//res.Body.Close()
//	//
//	//if err != nil {
//	//	panic(err)
//	//}
//	//return string(result)
//	return "helloworld"
//}


func download(r Retriever) string{
	// 下载器
	return r.Get("http://www.biquge.info")
}

func main() {
	var r Retriever
	r = baidu.A{}
	fmt.Println(download(r))
}

// 整理思路，其实interface接口只需要定义方法的定义而已。
// 而真正的方法实现可以通过struct结构体中定义方法来实现

