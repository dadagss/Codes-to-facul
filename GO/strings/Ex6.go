package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var str string
	fmt.Print("Digite uma string: ")

	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		str = scanner.Text()
	}

	palavras := strings.Fields(str)
	numPalavras := len(palavras)

	fmt.Printf("A string digitada contém %d palavra(s).\n", numPalavras)
}
