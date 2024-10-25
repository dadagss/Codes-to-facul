package main

import "fmt"

func main() {
	var (
		dias   int
		diaria int
	)
	fmt.Print("Você trabalhou por quantos dias?")
	fmt.Scan(&dias)
	fmt.Print("E quanto custa sua diaria?")
	fmt.Scan(&diaria)

	salario := dias * diaria

	fmt.Println("O seu salario será:", salario)
}
