package q2

import "testing"

func TestMaximumWealth(t *testing.T) {
	tests := []struct {
		accounts [][]int
		want     int
	}{
		{
			accounts: [][]int{
				{1, 2, 3},
				{3, 2, 1},
			},
			want: 6,
		},
		{
			accounts: [][]int{
				{1, 5},
				{7, 3},
				{3, 5},
			},
			want: 10,
		},
		{
			accounts: [][]int{
				{2, 8, 7},
				{7, 1, 3},
				{1, 9, 5},
			},
			want: 17,
		},
		{
			accounts: [][]int{
				{1},
			},
			want: 1,
		},
		{
			accounts: [][]int{
				{1, 2, 3, 5},
				{3, 2, 1, 4},
			},
			want: 11,
		},
		{
			accounts: [][]int{
				{1, 2, 3, 5},
				{3, 2, 1, 4},
				{1, 2, 3, 5, 8},
				{3, 2, 1, 4, 10},
				{3, 1, 4},
			},
			want: 20,
		},
		{
			accounts: [][]int{
				{1, 2, 3, 5},
				{3, 2, 1, 4},
				{1, 2, 3, 5, 8},
				{3, 2, 1, 4, 10},
				{3, 1, 4},
				{3, 1, 4, 5, 6, 7, 8, 9, 10},
			},
			want: 53,
		},
	}

	for _, test := range tests {
		result := MaximumWealth(test.accounts)
		if result != test.want {
			t.Errorf("MaximumWealth(%v) => %v,want %v", test.accounts, result, test.want)
		}
	}
}
