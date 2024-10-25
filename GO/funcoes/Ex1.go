package main

import "fmt"

func media(x []int) int {
	var (
		sum int
	)
	for _, y := range x {
		sum += y
	}
	return sum / len(x)
}

func main() {
	slice := []int{1, 2, 3, 4, 5}
	fmt.Println(media(slice))
}
