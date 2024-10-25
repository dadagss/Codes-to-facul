package q4

//Bob está se preparando para fazer um teste de QI. A tarefa mais frequente neste teste é descobrir qual dos n números
//dados difere dos outros. Bob observou que geralmente um número difere dos outros em relação à paridade (ser par ou
//ímpar). Ajude Bob - para verificar suas respostas, ele precisa de um programa que, entre os n números dados, encontre um
//que seja diferente em relação à paridade.

//Sua tarefa é retornar o índice do elemento que difere dos outros em relação à paridade.

func IQTest(numbers []int) int {
	d1 := 0
	d2 := 0
	b1 := -1
	b2 := -1

	for i, num := range numbers {
		if num%2 == 0 {
			d1++
			b1 = i
		} else {
			d2++
			b2 = i
		}
	}

	if d1 == 1 {
		return b1
	}

	if d2 == 1 {
		return b2
	}

	return -1
}

