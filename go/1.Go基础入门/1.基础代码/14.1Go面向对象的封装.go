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

// go mod的使用
// 使用原因：modules替换旧的基于GOPATH的方法来指定在给定构建中使用哪些源文件。
// 使用场景：如果不实用modules模块，那么所有的文件引入都要从GOPATH的路径的src路径中进行源文件的查找
//			而每一个项目不可能都存档在GOPATH/src路径中，因此go mod的使用可以快速的解决这个问题。


// go mod的使用方法
// 1. 在项目文件夹中使用"go mod init 名称"，用于初始化生成go.mod 文件
// 2. 创建api文件夹，以及apis.go文件
// 	apis.go中定义如下内容
//	package api
//
//	const (
//		Name = "王海飞"
//	)
//
//	func HelloWorld () string {
//		return "hello world"
//	}
// 3. 创建另外一个go文件，然后导入apis.go文件中定义的public方法HelloWorld
//	 导入定义为刚才使用"go mod ini 名称（如hello）" 中的名称（如hello)/包名(如api)，如"hello/api"
// 4. 如需使用apis.go中定义的public函数，则使用api.函数名()即可

func main () {

	fmt.Println(api.HelloWorld())
	fmt.Println(api.Name)
	fmt.Println(http.Cookie{})
}

