package main

import (
	"fmt"
	"strings"
)
import "bufio"
import "os"

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Escreva sua frase: ")
	scanner.Scan()
	frase := scanner.Text()
	println(strings.ToUpper(frase))
}
