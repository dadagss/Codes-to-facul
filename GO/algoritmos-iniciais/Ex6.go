package main

import "fmt"

func main() {
	var (
		Salario int
	)
	fmt.Print("Qual seu salario?")
	fmt.Scan(&Salario)

	ganho := (Salario*15)/100 + Salario

	fmt.Println("Com o aumento de nossa empresa você recebera:", ganho)
}
