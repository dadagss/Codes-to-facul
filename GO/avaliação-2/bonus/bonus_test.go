package bonus

import (
	"fmt"
	"testing"
)

func TestInvertLinkedList(t *testing.T) {
	tests := []struct {
		input []int
	}{
		{
			input: []int{1, 2, 3, 4, 5},
		},
		{
			input: []int{5, 2, 4, 6, 6, 2, 2},
		},
		{
			input: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
		},
		{
			input: []int{1, 23, 4, 5, 12, 123, 21, 525, 1236, 234, 12, 12},
		},
		{
			input: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14},
		},
		{
			input: []int{1},
		},
	}

	for _, test := range tests {
		t.Run(fmt.Sprintf("input=%v", test.input), func(t *testing.T) {
			head := createLinkedList(test.input)
			InvertLinkedList(head)
			if !isLinkedListInverted(head, test.input) {
				t.Errorf("linked list is not inverted")
			}
		})
	}
}

func isLinkedListInverted(head *LinkedList, original []int) bool {
	current := head.Head
	for i := len(original) - 1; i >= 0; i-- {
		if current.Value != original[i] {
			return false
		}
		current = current.Next
	}
	return true
}

func createLinkedList(input []int) *LinkedList {
	head := &LinkedList{
		Head: &Node{Value: input[0]},
	}
	current := head.Head
	for i := 1; i < len(input); i++ {
		current.Next = &Node{
			Value: input[i],
		}
		current = current.Next
	}
	return head

}
