package main

import "fmt"

func prim(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func Sli(x *[]int, n int) {
	count := 0
	num := 2
	for count < n {
		if prim(num) {
			*x = append(*x, num)
			count++
		}
		num++
	}
}
func main() {
	var s []int
	Sli(&s, 5)
	fmt.Println(s)

}
