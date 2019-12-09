package main

import "github.com/kataras/iris"

func main() {
	app := iris.New()

	// 生成模板引擎
	// iris.HTML(解析的文件路径，解析文件的后缀)
	htmlEngine := iris.HTML("./templates", ".html")
	// 注册模板引擎
	app.RegisterView(htmlEngine)

	app.Get("/hello", func(ctx iris.Context) {
		// 向前端页面中传递两个变量，title和data
		ctx.ViewData("title", "测试页面")
		ctx.ViewData("data", "hello world! 😂哈哈哈")
		// 指定渲染的页面
		ctx.View("hello.html")
	})
	// 启动
	app.Run(iris.Addr(":8080"))
}

