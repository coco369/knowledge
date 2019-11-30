package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	// if else的使用1
	contents, err := ioutil.ReadFile("abc.txt")
	// 如果返回的错误信息err为空，则其值为nil
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("%s\n", contents)
	}

	// if else的使用2
	const filename = "abc1.txt"
	if contens1, err1 :=ioutil.ReadFile(filename); err1 == nil {
		fmt.Println(string(contens1))
	} else {
		fmt.Println(err1)
	}
}