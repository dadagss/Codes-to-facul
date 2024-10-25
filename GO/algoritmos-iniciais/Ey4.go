package main

import "fmt"

func main() {
	var (
		altura float64
		peso   float64
		sexo   int
	)
	fmt.Print("Qual sua altura? ")
	fmt.Scan(&altura)
	fmt.Print("Qual o seu peso? ")
	fmt.Scan(&peso)
	fmt.Print("Qual o seu sexo? ")
	fmt.Scan(&sexo)

	IMC := peso / (altura * altura)

	if IMC < 18.5 {
		falta := IMC - 18.5
		fmt.Println("Falta ", falta, "para você alcançar o peso ideal")
	}
	if IMC > 24.9 {
		sobra := 24.9 - IMC
		fmt.Println("você esta", sobra, " acima do peso ideal")
	}

}
