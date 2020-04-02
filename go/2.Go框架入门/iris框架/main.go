package main

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/xormplus/xorm"
	"time"
)

/*
   pk表示主键 autoincr 自增
   如果Field名就叫做Id，并且类型为int64，如果不加tag，会自动被xorm视为主键，并且自增。
   如果想用Id以外、或者非int64类型作为主键，必须要显示的在tag中指定，`xorm:"pk autoincr"`
*/

type User struct {
	Id int64
	//User_id int64 `xorm:"pk autoincr"`
	Username string `xorm:"varchar(20) not null unique"`
	Password string `xorm:"varchar(200)"`
	CreateTime time.Time `xorm:"created"`
}

func main() {
	// 创建iris对象
	//app := iris.New()
	//// 创建模板引擎,解析当前文件夹的上层目录中的templates文件夹，并解析扩展名为.html结尾的文件
	//html = iris.HTML("../templates", ".html")
	//app.RegisterView(html)
	//// 指定静态文件夹，访问的路由前缀为/static时，将访问上层目录中的static文件夹
	//app.StaticWeb("/static", "../static")
	// 配置mysql数据库的连接
	engine, err := xorm.NewEngine("mysql", "root:wang135588@(127.0.0.1:3306)/gotest?charset=utf8")
	if err != nil {
		fmt.Printf("数据库连接失败：%s", err)
		return
	}
	u1 := new(User)
	u1.Username = "coco"
	u1.Password = "123456"
	affected, err :=engine.Insert(u1)
	if err != nil {
		fmt.Println(err, affected)
	}

	//app.Run(iris.Addr(":8080"))

}