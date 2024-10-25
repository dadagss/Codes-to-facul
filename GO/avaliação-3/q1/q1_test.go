package q1

import "testing"

func TestCountMatches(t *testing.T) {
	tests := []struct {
		items     []Item
		ruleKey   string
		ruleValue string
		want      int
	}{
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
				{
					Type:  "computer",
					Color: "silver",
					Name:  "lenovo",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
			},
			ruleKey:   "color",
			ruleValue: "silver",
			want:      2,
		},
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
				{
					Type:  "computer",
					Color: "silver",
					Name:  "lenovo",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
			},
			ruleKey:   "type",
			ruleValue: "phone",
			want:      2,
		},
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
				{
					Type:  "computer",
					Color: "silver",
					Name:  "lenovo",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
			},
			ruleKey:   "name",
			ruleValue: "lenovo",
			want:      1,
		},
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
			},
			ruleKey:   "color",
			ruleValue: "silver",
			want:      0,
		},
		{
			items:     []Item{},
			ruleKey:   "color",
			ruleValue: "silver",
			want:      0,
		},
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
				{
					Type:  "computer",
					Color: "silver",
					Name:  "lenovo",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
			},
			ruleKey:   "color",
			ruleValue: "silver",
			want:      3,
		},
		{
			items: []Item{
				{
					Type:  "phone",
					Color: "blue",
					Name:  "pixel",
				},
				{
					Type:  "computer",
					Color: "silver",
					Name:  "lenovo",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
				{
					Type:  "phone",
					Color: "silver",
					Name:  "iphone",
				},
			},
			ruleKey:   "color",
			ruleValue: "silver",
			want:      5,
		},
	}
	for _, test := range tests {
		if got := CountMatches(test.items, test.ruleKey, test.ruleValue); got != test.want {
			t.Errorf("CountMatches(%v, %v, %v) => %v,want %v", test.items, test.ruleKey, test.ruleValue, got, test.want)
		}
	}
}
