package bonus

import (
	"testing"
)

func TestMedianShirtPrice(t *testing.T) {
	tests := []struct {
		shirts  []Shirt
		want    float64
		wantErr bool
	}{
		{
			shirts: []Shirt{
				createShirt("M", 10.0),
				createShirt("M", 20.0),
				createShirt("M", 30.0),
				createShirt("XXXXXS", 30.0),
				createShirt("XXXXXS", 30.0),
				createShirt("XXXXXS", 30.0),
				createShirt("XXS", 350.0),
				createShirt("XXXS", 450.0),
				createShirt("S", 150.0),
				createShirt("S", 550.0),
			},
			want: 350,
		},
		{
			shirts: []Shirt{
				createShirt("M", 10.0),
				createShirt("M", 20.0),
				createShirt("M", 30.0),
				createShirt("XXXS", 30.0),
				createShirt("XXS", 30.0),
				createShirt("S", 30.0),
				createShirt("L", 40.0),
				createShirt("L", 50.0),
				createShirt("L", 60.0),
			},
			want: 30.0,
		},
		{
			shirts: []Shirt{
				createShirt("XXXXXXXXXS", 20.0),
				createShirt("XXS", 30.0),
				createShirt("XXXXXXXXXS", 30.0),
				createShirt("XXXXL", 40.0),
				createShirt("XXXXL", 50.0),
				createShirt("XXL", 60.0),
				createShirt("M", 160.0),
				createShirt("M", 60.0),
			},
			want: 110,
		},
		{
			shirts: []Shirt{
				createShirt("XXXXL", 40.0),
				createShirt("XXXXXXL", 50.0),
				createShirt("XXL", 30.0),
				createShirt("XXL", 20.0),
				createShirt("XXL", 25.0),
				createShirt("XXXXXXL", 55.0),
				createShirt("XXXXXXL", 60.0),
				createShirt("XXXXL", 60.0),
			},
			want: 50.0,
		},
		{
			shirts: []Shirt{
				createShirt("XXXXS", 40.0),
				createShirt("XXXXXXS", 50.0),
				createShirt("XXS", 30.0),
				createShirt("XXS", 20.0),
				createShirt("XXS", 25.0),
				createShirt("XXXXXXS", 55.0),
				createShirt("XXXXXXS", 60.0),
				createShirt("XXXXS", 60.0),
			},
			want: 50.0,
		},
		{
			shirts:  []Shirt{},
			wantErr: true,
		},
	}

	for _, test := range tests {
		result, err := MedianShirtPrice(test.shirts)
		if err != nil {
			if !test.wantErr {
				t.Errorf("MedianShirtPrice(%v) returned error %v", test.shirts, err)
			}
		} else if result != test.want {
			t.Errorf("MedianShirtPrice(%v) = %v, want %v", test.shirts, result, test.want)
		}
	}
}

func createShirt(s string, f float64) Shirt {
	return Shirt{
		Size:  s,
		Price: f,
	}
}
