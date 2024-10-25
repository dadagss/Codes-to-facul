package main

import "fmt"

func main() {
	var x, y int

	fmt.Print("qual o seu primeiro numero?")
	fmt.Scan(&x)
	fmt.Print("qual o seu segundo numero?")
	fmt.Scan(&y)
	if x > y {
		fmt.Println(x, "é maior que ", y)
	}
	if y > x {
		fmt.Println(y, "é maior que", x)
	}
}