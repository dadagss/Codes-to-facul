package main

import "fmt"

func main() {
	for i := 0; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%3 != 0 && i%5 == 5 {
			fmt.Println("Buzz")
		} else if i%3 == 0 && i%5 != 0 {
			fmt.Println("Fizz")
		} else {
			fmt.Println(i)
		}
	}
}
