package main

import "fmt"

func Soma(n *int) {
	x := 0
	sum := 0
	for x = 0; x <= *n; x++ {
		sum += x
	}
	*n = sum
}
func main() {
	n := 5
	ptr := &n
	Soma(ptr)
	fmt.Println(*ptr)

}
