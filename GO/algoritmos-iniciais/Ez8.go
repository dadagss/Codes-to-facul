package main

import "fmt"

func main() {
	var x int
	fmt.Print("Qual o seu número? ")
	fmt.Scan(&x)
	fmt.Println("os divisores de ", x, " são:")
	for i := 1; i <= x; i++ {
		if x%i == 0 {
			fmt.Println("Os divisores são")
		}
	}
}
