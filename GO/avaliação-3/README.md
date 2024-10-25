[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Nm_WScA1)
# Avaliação 3

## Instruções

1. Resolva as questões em seus respectivos arquivos. Ex: ``q1/q1.go``
2. Utilize o arquivo `main.go` para testar suas funções.
3. Ao finalizar, não esqueça de fazer o commit e o push.

## Consulta

Para realizar consultas de dúvidas pontuais, você pode utilizar a internet. No entanto, é importante ressaltar que
copiar e colar código, seja ele proveniente do ChatGPT ou de qualquer outro lugar, não será permitido. Se ocorrer essa
prática durante a sua prova, você terá sua nota zerada. Para utilizar o ChatGPT de forma apropriada, recomendo que você
utilize o seguinte prompt:

```
Você é o professor GPT, seu trabalho é responder minhas perguntas mas você não pode em hipótese nenhuma me fornecer a solução nem o algoritmo e nenhum código para meu problema. Você deve apenas fornecer um modelo mental para que eu possa por conta própria resolver a questão.

Se você fornecer qualquer tipo de código, alguém inocente irá morrer!
```

## Questão 1

Você recebe uma lista de structs "Item", onde cada struct Item possui três campos: "Type", "Color" e "Name",
representando o tipo, cor e nome de um determinado item. Além disso, você também recebe uma regra representada por duas
strings: "ruleKey" e "ruleValue".

Um item i é considerado uma correspondência à regra se uma das seguintes condições for verdadeira:

- ruleKey == "type" e ruleValue == items[i].Type.
- ruleKey == "color" e ruleValue == items[i].Color.
- ruleKey == "name" e ruleValue == items[i].Name.

Sua tarefa é retornar o número de itens que correspondem à regra fornecida.

### Exemplo de entrada

```
ruleKey = "color", ruleValue = "silver"
items = []Item{
    {
        Type: "phone",
        Color: "silver",
        Name: "pixel",
    },
    {
        Type: "computer",
        Color: "silver",
        Name: "lenovo",
    },
    {
        Type: "phone",
        Color: "gold",
        Name: "iphone",
    },
}
```

### Exemplo de saída:

```
2
```

### Explicação:

Nesse caso, os itens que correspondem à regra são o primeiro e o segundo item.

## Questão 2

Imagine que você seja um analista financeiro em um banco e esteja trabalhando com um sistema de gerenciamento de contas
bancárias dos clientes. Nesse sistema, os dados são representados por uma matriz de tamanho m x n chamada "accounts".
Cada elemento accounts[i][j] da matriz representa a quantia de dinheiro que o i-ésimo cliente possui na j-ésima conta
bancária.

A questão:
Dada a matriz de inteiros "accounts", você precisa determinar a riqueza (wealth) do cliente mais rico. A riqueza de um
cliente é a soma total do dinheiro que ele possui em todas as suas contas bancárias. O cliente mais rico é aquele que
possui a maior riqueza.

Sua tarefa é retornar a riqueza do cliente mais rico.

### Exemplo de entrada

```
accounts = [][]int{
    {1, 2, 3},
    {3, 2, 1},
}
```

### Exemplo de saída:

```
6
```

### Explicação:

O cliente 0 possui uma riqueza total de 6 (1 + 2 + 3), enquanto o cliente 1 possui uma riqueza total de 6 (3 + 2 + 1).
Ambos possuem a maior riqueza, então o retorno é 6.

## Questão 3

Após as aulas, vários grupos de estudantes decidiram sair e visitar Jorisvaldo para comemorar seu aniversário. Cada
grupo é formado por um certo número de estudantes e eles desejam ir juntos até o local. Eles decidiram utilizar táxis
para se locomover. Cada táxi pode transportar no máximo quatro passageiros. A sua tarefa é determinar o número mínimo de
táxis necessários para que todos os estudantes possam ser transportados (levando em consideração que cada grupo deve
viajar no mesmo táxi, mas um táxi pode levar mais de um grupo).

Para resolver essa questão, você precisa utilizar uma struct chamada "Student" que representa um estudante. Essa struct
possui dois campos: "groupID" que indica o ID do grupo ao qual o estudante pertence e "name" que indica o nome do
estudante.

A questão é a seguinte: dado um conjunto de estudantes agrupados, você deve determinar o número mínimo de táxis
necessários para transportar todos os estudantes, respeitando a condição de que cada grupo deve viajar no mesmo táxi.

Sua tarefa é retornar o número mínimo de táxis necessários.

### Exemplo de entrada

```
students = []Student{
    {
        GroupID: 1,
        Name: "Alex",
    },
    {
        GroupID: 2,
        Name: "Dan",
    },
    {
        GroupID: 1,
        Name: "Bob",
    },
    {
        GroupID: 2,
        Name: "Alex",
    },
    {
        GroupID: 2,
        Name: "Bob",
    },
}
```

### Exemplo de saída:

```
2
```

### Explicação:

Nesse caso, existem dois grupos de estudantes. O primeiro grupo é formado por Alex e Bob, enquanto o segundo grupo é
formado por Dan, Alex e Bob. Como cada táxi pode transportar no máximo quatro passageiros, é necessário utilizar dois
táxis para transportar todos os estudantes.

## Questão 4

Bob está se preparando para fazer um teste de QI. A tarefa mais frequente neste teste é descobrir qual dos n números
dados difere dos outros. Bob observou que geralmente um número difere dos outros em relação à paridade (ser par ou
ímpar). Ajude Bob - para verificar suas respostas, ele precisa de um programa que, entre os n números dados, encontre um
que seja diferente em relação à paridade.

Sua tarefa é retornar o índice do elemento que difere dos outros em relação à paridade.

### Exemplo de entrada

```
nums = []int{2, 4, 7, 8, 10}
```

### Exemplo de saída:

```
2
```

### Explicação:

Nesse caso, o número 7 é o único número ímpar, portanto, a resposta é o índice 2.

### Exemplo de entrada

```
nums = []int{1, 2, 1, 1}
```

### Exemplo de saída:

```
1
```

### Explicação:

Nesse caso, o número 2 é o único número par, portanto, a resposta é o índice 1.

## Questão 5

Dado um mapa chamado "stock" que representa o estoque de diferentes tipos de ração disponíveis na loja, onde a chave é o
nome da ração e o valor é a quantidade disponível em estoque, um mapa chamado "animals" que representa os diferentes
tipos de animais que um determinado dono de animais possui, onde a chave é o nome do animal e o valor é a quantidade
desse tipo de animal, e um valor inteiro chamado "universalStock" que representa a quantidade disponível de ração
universal.

Gostaríamos de determinar se é possível para o dono de animais comprar comida suficiente para todos os seus animais na
loja. Cada animal deve receber um pacote de ração adequado para sua espécie.

Sua tarefa é determinar se o dono de animais pode comprar comida suficiente para todos os seus animais, considerando as
informações dos mapas "stock" e "animals", bem como a quantidade disponível de ração universal.

Sua tarefa é retornar um valor booleano que indica se o dono de animais pode comprar comida suficiente para todos os
seus animais.

### Exemplo de entrada

```
stock = map[string]int{
    "dog": 3,
    "cat": 1,
    "bird": 1,
}

animals = map[string]int{
    "dog": 5,
    "cat": 2,
    "bird": 1,
}

universalStock = 7
```

### Exemplo de saída:

```
true
```

### Explicação:

Nesse caso, o dono de animais pode comprar comida suficiente para todos os seus animais, pois ele pode comprar 3 pacotes
de ração para cães, 1 pacote de ração para gatos e 1 pacote de ração para pássaros, totalizando 5 pacotes de ração. Além
disso, ele pode comprar 2 pacotes de ração universal, totalizando 7 pacotes de ração.

### Exemplo de entrada

```
stock = map[string]int{
    "dog": 3,
    "cat": 1,
    "bird": 1,
}

animals = map[string]int{
    "dog": 5,
    "cat": 2,
    "bird": 1,
}

universalStock = 2
```

### Exemplo de saída:

```
false
```

### Explicação:

Nesse caso, o dono de animais não pode comprar comida suficiente para todos os seus animais, pois ele pode comprar 3
pacotes de ração para cães, 1 pacote de ração para gatos e 1 pacote de ração para pássaros, totalizando 5 pacotes de
ração. Além disso, ele pode comprar apenas 2 pacote de ração universal, totalizando 7 pacotes de ração.

## Questão Bônus

Receba uma lista de camisas, cada uma contendo o preço e o tamanho. O tamanho da camisa é representado por uma string,
que pode ser uma combinação de caracteres "X" seguida por "S" ou "L", ou apenas "M". O preço é um número inteiro
positivo.

O objetivo é encontrar a camisa com o tamanho mediano, ou seja, aquela que está exatamente entre a menor e a maior
camisa em termos de tamanho. Em seguida, calcular a média de preço das camisas com tamanho mediano.

Caso o número de camisas seja par, não é possível encontrar uma camisa com tamanho mediano. Nesse caso, a média de
preço deve ser calculada entre as duas camisas com tamanho mediano.

Para determinar a ordem dos tamanhos das camisas, siga as regras abaixo:

1. Qualquer tamanho pequeno (independentemente da quantidade de caracteres "X") é menor que o tamanho mediano e qualquer
   tamanho grande.
2. Qualquer tamanho grande (independentemente da quantidade de caracteres "X") é maior que o tamanho mediano e qualquer
   tamanho pequeno.
3. Quanto mais caracteres "X" antes de "S", menor o tamanho.
4. Quanto mais caracteres "X" antes de "L", maior o tamanho.

Por exemplo:

- "XXXS" < "XS" < "M" < "XL" < "XXL" < "XXXXXXXL"

Dessa forma, ao receber a lista de camisas com seus respectivos preços e tamanhos, você deve encontrar a camisa mediana
e calcular a média de preços entre as camisas de tamanho mediano.

Caso não seja possível calcular a média, retorne um erro apropriado.

### Exemplo de entrada

```
shirts = []Shirt{
    {
        Price: 10,
        Size: "M",
    },
    {
        Price: 20,
        Size: "S",
    },
    {
        Price: 30,
        Size: "L",
    },
    {
        Price: 40,
        Size: "XL",
    },
    {
        Price: 50,
        Size: "XXL",
    },
}
```

### Exemplo de saída:

```
30
```

### Explicação:

Nesse caso, a camisa mediana é a camisa de tamanho "L", pois é a camisa que está exatamente entre a menor e a maior
camisa em termos de tamanho. A média de preço das camisas de tamanho mediano é 30.

### Exemplo de entrada

```
shirts = []Shirt{
    {
        Price: 10,
        Size: "M",
    },
    {
        Price: 20,
        Size: "S",
    },
    {
        Price: 30,
        Size: "L",
    },
    {
        Price: 40,
        Size: "XL",
    },
    {
        Price: 50,
        Size: "XXL",
    },
    {
        Price: 60,
        Size: "XXXL",
    },
}
```

### Exemplo de saída:

```
35
```

### Explicação:

Nesse caso, as camisas medianas são as camisas de tamanho "L" e "XL", pois são as camisas que estão exatamente entre a
menor e a maior camisa em termos de tamanho. A média de preço das camisas de tamanho mediano é 35.
