package main

import "fmt"

func SSum(ptr *int) {
	if ptr == nil {
		fmt.Errorf("O ponteiro é nulo")
	}
	*ptr = 42
}
func main() {
	num := 0
	ptr := &num
	SSum(ptr)
	fmt.Println(*ptr)
}
