package main

import "fmt"

type conta struct {
	saldo   float64
	titular string
}

func Sum(x *conta) {
	sal := &x.saldo
	var new float64
	fmt.Println("Deseja adicionar saldo a conta?")
	fmt.Scan(&new)
	*sal += new
}

func main() {
	cont := conta{saldo: 50.0, titular: "Daniel"}
	ptr := &cont
	Sum(ptr)
	fmt.Println(*ptr)

}
