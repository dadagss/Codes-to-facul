package main

import "fmt"
import "strings"

func main() {
	var (
		str string
		x   string
		y   string
	)

	fmt.Print("Qual sua palavra: ")
	fmt.Scan(&str)
	fmt.Print("Deseja substituir qual caracter?")
	fmt.Scan(&x)
	fmt.Print("Deseja substituir por qual?")
	fmt.Scan(&y)
	subs := strings.ReplaceAll(str, x, y)
	fmt.Printf("Sua palavra sem a letra %s e com a letra %s ficou: %s", x, y, subs)

}
