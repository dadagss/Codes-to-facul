package main

import "fmt"

func main() {
	var (
		numero int
	)
	fmt.Print("Qual o seu numero")
	fmt.Scan(&numero)

	antecessor := numero - 1
	sucessor := numero + 1

	fmt.Println("O antecessor do seu número é:", antecessor, ",e o sucessor é:", sucessor)
}
