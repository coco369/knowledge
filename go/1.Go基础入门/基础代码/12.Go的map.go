package main

import "fmt"

// map，map的定义为: map[k的类型]v的类型 {k:v, k1:v1....}

func main () {
	// 创建方法1
	m := map[string] string {
		"name": "wanghaifei",
		"age": "18",
		"gender": "man",
	}
	fmt.Println(m)

	// 创建方法2
	m2 := make(map[string] string)
	fmt.Println(m2)

	// 创建方法3
	var m3 map[string] string
	fmt.Println(m3)

	// 注意map的key和value获取时，打印是无序的
	// 遍历获取key和value
	for k,v := range m {
		fmt.Println(k, v)
	}
	// 遍历获取value
	for _, v := range m {
		fmt.Println(v)
	}
	// 遍历获取key
	for k := range m {
		fmt.Println(k)
	}

	// 通过key获取value。如果获取一个不存在的key值，则返回空""
	fmt.Println("通过key获取value")
	m4 := m["name1"]
	if m4 == "" {
		fmt.Println("空")
	} else {
		fmt.Println(m4)
	}

	// 判断某一个key是否存在于map中
	// 如果key存在，则ok为true，否则ok为false
	m5, ok := m["name"]
	fmt.Println(m5, ok)

	if m6, ok := m["gender"]; ok {
		fmt.Println(m6)
	} else {
		fmt.Println("key:gender不存在")
	}

	// 删除元素
	name, ok := m["name"]
	fmt.Println(name, ok)

	fmt.Println("删除m中的name之前")
	// delete(map, "键")： 删除map中的键值对
	delete(m, "name")

	fmt.Println("删除m中的name之后")
	name, ok = m["name"]
	fmt.Println(name, ok)
}
