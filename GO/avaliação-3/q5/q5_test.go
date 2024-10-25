package q5

import (
	"testing"
)

func TestCanBuyAllFood(t *testing.T) {
	tests := []struct {
		stock     map[string]int
		animals   map[string]int
		universal int
		want      bool
	}{
		{
			stock: map[string]int{
				"chicken": 1,
				"cat":     1,
				"dog":     1,
			},
			animals: map[string]int{
				"chicken": 1,
				"cat":     1,
			},
			universal: 1,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  4,
				"cat":  2,
				"bird": 3,
			},
			animals: map[string]int{
				"dog": 4,
				"cat": 2,
			},
			universal: 1,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  4,
				"cat":  2,
				"bird": 3,
			},
			animals: map[string]int{
				"dog": 6,
				"cat": 2,
			},
			universal: 1,
			want:      false,
		},
		{
			stock: map[string]int{},
			animals: map[string]int{
				"dog": 5,
				"cat": 3,
			},
			universal: 0,
			want:      false,
		},
		{
			stock: map[string]int{},
			animals: map[string]int{
				"dog": 5,
				"cat": 3,
			},
			universal: 8,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
			},
			animals: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
			},
			universal: 0,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
			},
			animals: map[string]int{
				"dog":     5,
				"cat":     3,
				"chicken": 2,
			},
			universal: 0,
			want:      false,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
			},
			animals: map[string]int{
				"dog":     5,
				"cat":     3,
				"chicken": 2,
			},
			universal: 2,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
			},
			animals: map[string]int{
				"dog":     4,
				"cat":     3,
				"chicken": 1,
				"cow":     1,
			},
			universal: 3,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
				"a":    1,
				"b":    1,
				"c":    1,
				"d":    1,
				"e":    1,
				"f":    1,
				"g":    1,
				"h":    1,
				"i":    1,
				"j":    1,
				"k":    1,
				"l":    1,
				"m":    1,
				"n":    1,
				"o":    1,
				"p":    1,
				"q":    1,
				"r":    1,
				"s":    1,
				"t":    1,
				"u":    1,
				"v":    1,
				"w":    1,
				"x":    1,
				"y":    1,
				"z":    1,
			},
			animals: map[string]int{
				"dog":     4,
				"cat":     3,
				"chicken": 1,
				"a":       1,
				"b":       1,
				"c":       1,
				"d":       1,
				"e":       1,
				"f":       1,
				"g":       1,
				"h":       1,
				"i":       1,
				"j":       1,
				"k":       1,
				"l":       1,
				"m":       1,
				"n":       1,
				"o":       1,
				"p":       1,
				"q":       1,
				"r":       1,
				"s":       1,
				"t":       1,
				"u":       1,
				"v":       1,
				"w":       1,
				"x":       1,
				"y":       1,
				"z":       1,
			},
			universal: 3,
			want:      true,
		},
		{
			stock: map[string]int{
				"dog":  5,
				"cat":  3,
				"bird": 2,
				"a":    1,
				"b":    1,
				"c":    1,
				"d":    1,
				"e":    1,
				"f":    1,
				"g":    1,
				"h":    1,
				"i":    1,
				"j":    1,
				"k":    1,
				"l":    1,
				"m":    1,
				"n":    1,
				"o":    1,
				"p":    1,
				"q":    1,
				"s":    1,
				"u":    1,
				"v":    1,
				"w":    1,
				"x":    1,
				"y":    1,
				"z":    1,
			},
			animals: map[string]int{
				"dog":     5,
				"cat":     3,
				"chicken": 1,
				"a":       1,
				"b":       1,
				"c":       1,
				"d":       1,
				"e":       1,
				"f":       1,
				"g":       1,
				"h":       1,
				"i":       1,
				"j":       1,
				"k":       1,
				"l":       1,
				"m":       1,
				"n":       1,
				"o":       1,
				"p":       1,
				"q":       1,
				"r":       1,
				"s":       1,
				"t":       1,
				"u":       1,
				"v":       1,
				"w":       1,
				"x":       1,
				"y":       1,
				"z":       1,
			},
			universal: 1,
			want:      false,
		},
	}

	for _, tc := range tests {
		got := CanBuyAllFood(tc.stock, tc.animals, tc.universal)
		if got != tc.want {
			t.Errorf("CanBuyAllFood(%v, %v, %v) = %v; want %v", tc.stock, tc.animals, tc.universal, got, tc.want)
		}
	}
}
