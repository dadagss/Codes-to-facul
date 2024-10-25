package q5

//Dado um mapa chamado "stock" que representa o estoque de diferentes tipos de ração disponíveis na loja, onde a chave é o
//nome da ração e o valor é a quantidade disponível em estoque, um mapa chamado "animals" que representa os diferentes
//tipos de animais que um determinado dono de animais possui, onde a chave é o nome do animal e o valor é a quantidade
//desse tipo de animal, e um valor inteiro chamado "universalStock" que representa a quantidade disponível de ração
//universal.
//
//Gostaríamos de determinar se é possível para o dono de animais comprar comida suficiente para todos os seus animais na
//loja. Cada animal deve receber um pacote de ração adequado para sua espécie.
//
//Sua tarefa é determinar se o dono de animais pode comprar comida suficiente para todos os seus animais, considerando as
//informações dos mapas "stock" e "animals", bem como a quantidade disponível de ração universal.
//
//Sua tarefa é retornar um valor booleano que indica se o dono de animais pode comprar comida suficiente para todos os
//seus animais.

func CanBuyAllFood(stock map[string]int, animals map[string]int, universalStock int) bool {
	for _, animal := range animals {
		for _, quantidade := range stock {
			if animal != quantidade {
				if universalStock < quantidade {
					return false
				}
			}
			if animal+universalStock < quantidade {
				return false
			}
		}
	}
	return true
}
