package main

import (
	"fmt"
	"strconv"
)

func main() {
	var (
		str string
	)
	fmt.Println("Qual sua palavra?")
	fmt.Scan(&str)
	_, err := strconv.ParseFloat(str, 64)
	if err != nil {
		fmt.Printf("%s não é um número válido em ponto flutuante.\n", str)
	} else {
		fmt.Printf("%s é um número válido em ponto flutuante.\n", str)
	}
}
