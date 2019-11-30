package main

import "fmt"

func grade(score int) (string, error) {
	g := ""
	// switch后面可以不用加表达式，表达式写在case中就可以了
	switch {
	case score < 0 || score > 100:
		// panic 用于报错，不让程序继续往下执行
		return "F", fmt.Errorf("输入的参数有错误")
	case score < 60:
		g = "F"
	case score < 80:
		g = "C"
	case score < 90:
		g = "B"
	case score < 100:
		g = "A"
	}
	return g, nil
}

func main () {

	fmt.Println(grade(919))
}