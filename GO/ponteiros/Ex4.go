package main

import "fmt"

func sum(x *int) {
	var (
		valor1 int
		valor2 int
	)
	if *x > 100 {
		valor1 = (*x / 10) % 10
		valor2 = (*x % 10)
	} else {
		valor1 = 0
		valor2 = *x % 10
	}
	*x = valor1 + valor2
}
func main() {
	x := 1234
	ptr := &x
	sum(ptr)
	fmt.Println(*ptr)

}
