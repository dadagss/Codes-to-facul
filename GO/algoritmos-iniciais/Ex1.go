package main

import "fmt"

func main() {

	var (
		x1 int
		x2 int
		x3 int
	)

	fmt.Print("Qual o primeiro numero?")
	fmt.Scan(&x1)
	fmt.Print("Qual o segundo numero?")
	fmt.Scan(&x2)
	fmt.Print("Qual o terceiro numero?")
	fmt.Scan(&x3)

	Soma := x1 + x2 + x3
	fmt.Println("A soma dos inteiros é:", Soma)
}
