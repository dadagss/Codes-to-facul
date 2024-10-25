package main

import "fmt"

type livro struct {
	titulo string
	autor  string
	preço  float64
}

func desc(x *livro) {
	pre := &x.preço
	*pre = x.preço - (x.preço * 0.1)
}

func main() {
	cronicas := livro{titulo: "Dani", autor: "Daniel", preço: 543.93}
	ptr := &cronicas
	desc(ptr)
	fmt.Println(*ptr)
}
