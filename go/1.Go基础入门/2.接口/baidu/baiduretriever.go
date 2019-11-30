package baidu

import (
	"net/http"
	"net/http/httputil"
)

type A struct {
	UserAgent string
}


// 定义结构体中的方法，定义格式为func (变量 结构体名) 方法名 (参数) 返回参数类型 {}
func (a A) Get(url string) string {
	res, err := http.Get(url)
	if err != nil{
		panic(err)
	}

	result, err := httputil.DumpResponse(res, true)
	res.Body.Close()

	if err != nil {
		panic(err)
	}
	return string(result)
}