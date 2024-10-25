package main

import "fmt"

func main() {
	var idade int

	fmt.Print("Quantos anos você tem?")
	fmt.Scan(&idade)

	dias := idade * 365

	fmt.Println("Você tem ", dias, "dias de vida")

}
