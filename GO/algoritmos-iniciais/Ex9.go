package main

import "fmt"

func main() {

	var (
		preço int
	)
	fmt.Print("Qual o preço do seu produto:")
	fmt.Scan(&preço)

	desconto := preço - (preço*10)/100

	fmt.Println("O preço do seu produto sera", desconto)
}
