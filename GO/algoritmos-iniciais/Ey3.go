package main

import "fmt"

func main() {
	var x int

	fmt.Print("qual o seu primeiro numero?")
	fmt.Scan(&x)
	if x%2 == 0 {
		fmt.Print("o numero é par")
	} else {
		fmt.Println("o numero é impar")
	}

}
