package main

import "fmt"

func main() {
	var x, maior int
	fmt.Print("digite seus números abaixo: ")
	for {
		fmt.Scan(&x)
		if x == 0 {
			break
		}
		if x > maior {
			maior = x
		}
	}
	fmt.Printf("o maior numero foi %d\n", maior)
}
