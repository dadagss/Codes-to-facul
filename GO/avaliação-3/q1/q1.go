package q1

//Você recebe uma lista de structs "Item", onde cada struct Item possui três campos: "Type", "Color" e "Name",
//representando o tipo, cor e nome de um determinado item. Além disso, você também recebe uma regra representada por duas
//strings: "ruleKey" e "ruleValue".
//
//Um item i é considerado uma correspondência à regra se uma das seguintes condições for verdadeira:
//
//- ruleKey == "type" e ruleValue == items[i].Type.
//- ruleKey == "color" e ruleValue == items[i].Color.
//- ruleKey == "name" e ruleValue == items[i].Name.
//
//Sua tarefa é retornar o número de itens que correspondem à regra fornecida.

type Item struct {
	Type  string
	Color string
	Name  string
}

func CountMatches(items []Item, ruleKey string, ruleValue string) int {
	salada := 0
	for _, James := range items {
		if ruleKey == "type" && ruleValue == James.Type {
			salada++
		} else if ruleKey == "color" && ruleValue == James.Color {
			salada++
		} else if ruleKey == "name" && ruleValue == James.Name {
			salada++
		}

	}

	return salada
}
