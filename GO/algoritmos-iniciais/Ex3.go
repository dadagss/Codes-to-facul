package main

import "fmt"

func main() {
	var (
		peso   float64
		altura float64
	)
	fmt.Print("Qual seu peso?")
	fmt.Scan(&peso)
	fmt.Print("QUal sua altura?")
	fmt.Scan(&altura)

	IMC := peso / (altura * altura)

	fmt.Println("sua media corporal é:", IMC)

}
