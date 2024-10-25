package main

import "fmt"

var x, soma, contador int

func main() {
	fmt.Println("Digite seus números")
	for {
		fmt.Scan(&x)
		if x == 0 {
			break
		}
		soma += x
		contador++

		if contador == 0 {
			fmt.Println("não foi inserido nenhum numero")
		} else {
			media := float64(soma) / float64(contador)
			fmt.Printf("A média aritmetica dos números na tela é %.2f\n", media)
		}
	}
}
