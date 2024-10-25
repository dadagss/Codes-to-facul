package main

import "fmt"

type Livro struct {
	autor  string
	titulo string
}

func Name(x *Livro) {
	paut := x.autor
	ptit := &x.titulo
	if paut == "Anônimo" {
		*ptit = "Desconhecido"
	}
}
func main() {
	danram := Livro{autor: "Anônimo", titulo: "As cronicas de Danram"}
	ptr := &danram
	Name(ptr)
	fmt.Println(*ptr)
}
