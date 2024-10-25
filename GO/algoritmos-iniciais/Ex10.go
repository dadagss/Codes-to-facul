package main

import "fmt"

func main() {
	var (
		kilos float64
	)
	fmt.Print("Quantos kilos você pesa?")
	fmt.Scan(&kilos)

	libras := kilos * 2.2046
	fmt.Println("O seu peso em libras sera:", libras)
}
