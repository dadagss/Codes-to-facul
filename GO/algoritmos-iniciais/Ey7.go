package main

import "fmt"

func main() {

	var (
		salario uint
	)
	fmt.Print("Qual o seu salario?")
	fmt.Scan(&salario)

	if salario < 1000 {
		aumento := (salario/100)*10 + salario
		fmt.Println("o aumento do seu salario foi de", aumento)
	}
	if salario > 1000 {
		aumento := (salario/100)*5 + salario
		fmt.Println("O aumento do seu salario foi de", aumento)
	}
}
