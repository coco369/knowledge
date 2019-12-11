package main

import "github.com/kataras/iris"

func main() {
	// 创建iris对象
	app := iris.New()
	// 创建模板引擎,解析当前文件夹的上层目录中的templates文件夹，并解析扩展名为.html结尾的文件
	html = iris.HTML("../templates", ".html")
	app.RegisterView(html)
	// 指定静态文件夹，访问的路由前缀为/static时，将访问上层目录中的static文件夹
	app.StaticWeb("/static", "../static")


	app.Run(iris.Addr(":8080"))

}