package baidu

import (
	"net/http"
	"net/http/httputil"
)

type A struct {
	UserAgent string
}

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