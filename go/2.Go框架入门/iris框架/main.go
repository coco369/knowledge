package main

import (
	"github.com/kataras/iris"
)

func main() {
	// 生成iris对象
	app := iris.New()

	// 定义路由和方法的关联关系
	app.Get("/hello", func(ctx iris.Context) {
		// 写入返回给前端的数据："hello world"
		ctx.WriteString("hello world")
	})

	// 启动，并指定启动的端口为8090
	app.Run(iris.Addr(":8090"))

}