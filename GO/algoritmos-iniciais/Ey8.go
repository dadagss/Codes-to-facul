package main

import "fmt"

func main() {
	var dia uint
	fmt.Print("Qual o dia?")
	fmt.Scan(&dia)

	switch dia {
	case 1:
		fmt.Print("hoje é domingo")
	case 2:
		fmt.Print("hoje é segunda")
	case 3:
		fmt.Print("hoje é terça")
	case 4:
		fmt.Print("Hoje é quarta")
	case 5:
		fmt.Print("hoje é quinta")
	case 6:
		fmt.Print("hoje é sexta")
	case 7:
		fmt.Print("hoje é sabado")

	}
}
