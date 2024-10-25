package q4

import (
	"testing"
)

func TestIQTest(t *testing.T) {
	tests := []struct {
		numbers  []int
		expected int
	}{
		{
			numbers:  []int{1, 2, 3, 7, 9, 11},
			expected: 1,
		},
		{
			numbers:  []int{2, 4, 7, 8, 10},
			expected: 2,
		},
		{
			numbers:  []int{1, 2, 1, 1},
			expected: 1,
		},
		{
			numbers:  []int{1, 2, 2},
			expected: 0,
		},
		{
			numbers:  []int{1, 2, 1, 1, 1, 1, 1, 1, 1, 1},
			expected: 1,
		},
		{
			numbers:  []int{1, 3, 1, 7, 1, 1, 1, 1, 1, 2},
			expected: 9,
		},
		{
			numbers:  []int{1, 3, 1, 7, 1, 1, 1, 1, 1, 1, 8},
			expected: 10,
		},
		{
			numbers:  []int{1, 3, 1, 7, 1, 1, 1, 1, 1, 1, 8, 9},
			expected: 10,
		},
		{
			numbers:  []int{2, 6, 8, 10, 3},
			expected: 4,
		},
		{
			numbers:  []int{2, 6, 8, 10, 30, 11},
			expected: 5,
		},
		{
			numbers:  []int{2, 6, 8, 10, 30, 11, 12},
			expected: 5,
		},
		{
			numbers:  []int{10, 2, 6, 8, 10, 30, 11, 12, 24, 48},
			expected: 6,
		},
	}

	for _, tc := range tests {
		result := IQTest(tc.numbers)
		if result != tc.expected {
			t.Errorf("IQTest(%v) = %d, want %d.", tc.numbers, result, tc.expected)
		}
	}
}
