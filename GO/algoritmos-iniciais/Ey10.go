package main

import "fmt"

func main() {
	var idade int

	fmt.Print("Qual sua idade?")
	fmt.Scan(&idade)

	if idade < 9 {
		fmt.Println("Mirim")
	} else if idade < 13 {
		fmt.Println("infantil")
	} else if idade < 17 {
		fmt.Println("juvenil")
	} else if idade >= 18 {
		fmt.Println("adulto")
	}

}
