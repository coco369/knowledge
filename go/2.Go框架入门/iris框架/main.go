package main

import "github.com/kataras/iris"


func main() {
	app := iris.New()
	app.Get("/", func(ctx iris.Context){})
	app.Run(iris.Addr(":8081"))
}