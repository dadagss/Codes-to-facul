package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var y int
	var z string
	var s string
	var tentativas []int
	var mtentativas [][]int

	for z != "n" {
		x := rand.Intn(101)
		count := 0
		for y != x {
			fmt.Println("Chute um numero entre 0 e 100!")
			fmt.Scan(&y)

			if y > x {
				fmt.Println("Seu número é maior que a resposta")
				count++
			} else if y < x {
				fmt.Println("Seu número é menor que a respota")
				count++
			}
			if y == x {
				count++
			}

		}
		tentativas = append(tentativas, count)
		mtentativas = append(mtentativas, tentativas)
		fmt.Println("Parabéns você acertou!")
		fmt.Printf("Você levou %d tentativas para acertar o número!", tentativas)
		fmt.Println("Deseja ver o número de tentativas utilizadas em cada rodada?(s/n)")
		fmt.Scan(&s)
		if s == "s" {
			for _, t := range mtentativas {
				fmt.Println(t)
			}
			fmt.Println("Deseja jogar novamente?(s/n)")
			fmt.Scan(&z)
			if z == "s" {
				tentativas = nil
				y = -1
			}
		}
	}

}