package main

import "fmt"

func main() {

	var (
		peso1 int
		peso2 int
		peso3 int
	)
	peso1 = 2
	peso2 = 3
	peso3 = 5
	var (
		x1 int
		x2 int
		x3 int
	)

	fmt.Print("Qual o primeiro número?")
	fmt.Scan(&x1)
	fmt.Print("QUal o segundo número?")
	fmt.Scan(&x2)
	fmt.Print("Qual o terceiro número?")
	fmt.Scan(&x3)

	média1 := (x1+x2+x3)/peso1 + peso2 + peso3

	fmt.Println("As médias ponderadas são respectivamente:", média1)
}
