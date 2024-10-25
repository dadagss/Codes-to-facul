package bonus

//Receba uma lista de camisas, cada uma contendo o preço e o tamanho. O tamanho da camisa é representado por uma string,
//que pode ser uma combinação de caracteres "X" seguida por "S" ou "L", ou apenas "M". O preço é um número inteiro
//positivo.
//
//O objetivo é encontrar a camisa com o tamanho mediano, ou seja, aquela que está exatamente entre a menor e a maior
//camisa em termos de tamanho. Em seguida, calcular a média de preço das camisas com tamanho mediano.
//
//Caso o número de camisas seja par, não é possível encontrar uma camisa com tamanho mediano. Nesse caso, a média de
//preço deve ser calculada entre as duas camisas com tamanho mediano.
//
//Para determinar a ordem dos tamanhos das camisas, siga as regras abaixo:
//
//1. Qualquer tamanho pequeno (independentemente da quantidade de caracteres "X") é menor que o tamanho mediano e qualquer
//   tamanho grande.
//2. Qualquer tamanho grande (independentemente da quantidade de caracteres "X") é maior que o tamanho mediano e qualquer
//   tamanho pequeno.
//3. Quanto mais caracteres "X" antes de "S", menor o tamanho.
//4. Quanto mais caracteres "X" antes de "L", maior o tamanho.
//
//Por exemplo:
//
//- "XXXS" < "XS" < "M" < "XL" < "XXL" < "XXXXXXXL"
//
//Dessa forma, ao receber a lista de camisas com seus respectivos preços e tamanhos, você deve encontrar a camisa mediana
//e calcular a média de preços entre as camisas de tamanho mediano.
//
//Caso não seja possível calcular a média, retorne um erro apropriado.

type Shirt struct {
	Price float64
	Size  string
}

func MedianShirtPrice(shirts []Shirt) (float64, error) {
	return 0, nil
}
