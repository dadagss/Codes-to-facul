package main

import "fmt"

func main() {
	var x int
	fmt.Print("Qual o seu numero? ")
	fmt.Scan(&x)

	if x%3 == 0 && x%5 == 0 {
		fmt.Print("seu numero é divisivel por 3 e por 5")
	}
	if x%3 == 0 && x%5 != 0 {
		fmt.Print("seu numero é divisivel apenas por 3")
	}
	if x%3 != 0 && x%5 == 0 {
		fmt.Print("Seu numero é divisivel apenas por 5")
	}
	if x%3 != 0 && x%5 != 0 {
		fmt.Print("Seu numero não é divisivel por nenhum dos dois")
	}
}
