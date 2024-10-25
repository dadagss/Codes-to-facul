package main

import "fmt"

func main() {
	var (
		str  string
		str1 string
	)

	fmt.Print("Qual sua primeira palavra?")
	fmt.Scan(&str)
	fmt.Print("Qual a sua segunda palavra?")
	fmt.Scan(&str1)

	if str == str1 {
		fmt.Println("Ambas são iguais")
	} else {
		fmt.Println("Ambas são diferentes")
	}

}
