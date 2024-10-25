package main

import "fmt"

func main() {
	var (
		x int
		y int
	)
	fmt.Print("Qual o seu primeiro numero?")
	fmt.Scan(&x)
	fmt.Print("Qual o seu segundo numero?")
	fmt.Scan(&y)

	if x < 0 || y < 0 {
		soma := x + y
		fmt.Println("a soma é:", soma)
	} else {
		multi := x * y
		fmt.Println("A multiplicação é:", multi)
	}

}
