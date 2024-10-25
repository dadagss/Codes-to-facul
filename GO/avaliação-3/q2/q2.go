package q2

//Imagine que você seja um analista financeiro em um banco e esteja trabalhando com um sistema de gerenciamento de contas
//bancárias dos clientes. Nesse sistema, os dados são representados por uma matriz de tamanho m x n chamada "accounts".
//Cada elemento accounts[i][j] da matriz representa a quantia de dinheiro que o i-ésimo cliente possui na j-ésima conta
//bancária.
//
//A questão:
//Dada a matriz de inteiros "accounts", você precisa determinar a riqueza (wealth) do cliente mais rico. A riqueza de um
//cliente é a soma total do dinheiro que ele possui em todas as suas contas bancárias. O cliente mais rico é aquele que
//possui a maior riqueza.
//
//Sua tarefa é retornar a riqueza do cliente mais rico.

func MaximumWealth(accounts [][]int) int {
	Ricao := 0

	for _, sub := range accounts {
		var conta int

		for _, marino := range sub {
			conta += marino
		}
		if conta > Ricao {
			Ricao = conta
		}
	}
	return Ricao
}
