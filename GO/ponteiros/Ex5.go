package main

import (
	"fmt"
	"math"
)

func dan(x *float64) {
	*x = (*x / math.Pi) / 2
}
func main() {
	X := 2.1234
	ptr := &X
	dan(ptr)
	fmt.Println(*ptr)
}
