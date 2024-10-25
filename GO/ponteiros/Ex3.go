package main

import "fmt"

func str(x *string) {
	b := []rune(*x)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	*x = string(b)
}
func main() {
	d := "danram"
	fmt.Println("normal", d)
	str(&d)
	fmt.Println("inverso", d)
}
