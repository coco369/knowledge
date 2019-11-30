package interface_combination

type A struct {
	name string
}


func (a A) Get(url string) string {
	return "结构体A的get方法"
}

func (b A) Div(a, c int) int {
	return a / c
}


func (c A) Print(msg string) string {
	return msg
}

