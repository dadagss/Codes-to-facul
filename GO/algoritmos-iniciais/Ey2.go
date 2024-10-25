package main

import "fmt"

func main() {
	var x, y, z int

	fmt.Print("qual o seu primeiro numero?")
	fmt.Scan(&x)
	fmt.Print("qual o seu segundo numero?")
	fmt.Scan(&y)
	fmt.Print("qual o seu terceiro numero?")
	fmt.Scan(&z)

	if x < y && x < z {
		fmt.Println(x, " é o menor numero")
	}
	if y < x && y < z {
		fmt.Println(y, " é o menor numero")
	}
	if z < x && z < y {
		fmt.Println(z, " é o menor numero")
	}
}
