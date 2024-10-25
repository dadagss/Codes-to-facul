package main

import "fmt"

func Joken(x *int) {
	if *x%2 == 0 {
		*x = 0
	} else {
		*x = 1
	}
}
func main() {
	x := 11
	ptr := &x
	Joken(ptr)
	fmt.Println(*ptr)
}
