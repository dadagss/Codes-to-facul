package bonus

//Implemente uma função que inverta
//uma [lista encadeada](https://www.ime.usp.br/~pf/algoritmos/aulas/lista.html#:~:text=Uma%20lista%20encadeada%20%C3%A9%20uma,segunda%2C%20e%20assim%20por%20diante),
//ou seja, altere a ordem dos elementos da lista de forma reversa.

type Node struct {
	Value int
	Next  *Node
}

type LinkedList struct {
	Head *Node
}

func InvertLinkedList(list *LinkedList) {
	var prev *Node = nil
	current := list.Head

	for current != nil {
		next := current.Next
		current.Next = prev
		prev = current
		current = next
	}
	list.Head = prev
}
