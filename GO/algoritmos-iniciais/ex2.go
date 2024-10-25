package main

import "fmt"

func main() {
	var (
		x1 int
	)
	fmt.Print("Digite o seu inteiro")
	fmt.Scan(&x1)

	Dobro := x1 * x1
	Triplo := x1 * x1 * x1
	Quadruplo := x1 * x1 * x1 * x1

	fmt.Println("O dobro do seu numero é:", Dobro)
	fmt.Println("O Triplo do seu numero é:", Triplo)
	fmt.Println("O quadruplo do seu numero é:", Quadruplo)
}
