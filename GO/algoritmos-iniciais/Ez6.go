package main

import "fmt"

func main() {
	var x int

	fmt.Print("Qual o seu numero")
	fmt.Scan(&x)

	for i := 1; i <= 10; i++ {
		resultado := x * i
		fmt.Printf("%d x %d = %d\n", x, i, resultado)
	}
}
