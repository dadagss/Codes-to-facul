package main

import "fmt"

func main() {
	var (
		x int
		y int
		z int
	)
	fmt.Print("Qual o seu primeiro número? ")
	fmt.Scan(&x)
	fmt.Print("Qual o seu segundo número? ")
	fmt.Scan(&y)
	fmt.Print("Qual o seu terceiro numero?")
	fmt.Scan(&z)

	if x > y && x > z {
		fmt.Printf("%d > %d > %d", x, z, y)
	} else {
		fmt.Printf("%d > %d > %d", y, z, x)
	}
	if y > x && y > z {
		fmt.Printf("%d > %d > %d", y, x, z)
	} else {
		fmt.Printf("%d > %d > %d", y, z, x)
	}
	if z > x && z > y {
		fmt.Printf("%d > %d > %d", z, x, y)
	} else {
		fmt.Printf("%d > %d > %d", z, y, x)
	}
}
