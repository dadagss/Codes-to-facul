package main

import (
	"fmt"
	"strings"
)

func vogais(str string) int {
	vogais := "aeiouAEIOU"
	quantidade := 0
	for _, letra := range str {
		if strings.ContainsRune(vogais, letra) {
			quantidade++
		}
	}
	return quantidade
}

func main() {
	str := "Daniel"
	fmt.Println(vogais(str))

}
