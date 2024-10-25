package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Escreva uma frase ")
	scanner.Scan()
	frase := scanner.Text()
	frasecompl := strings.ReplaceAll(frase, " ", "")

	fmt.Printf("sua string sem espaço é %s", frasecompl)
}
