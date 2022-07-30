"""
Exercício 01

1 - Criar uma classe chamada Container. Essa classe terá um atributo de nome "espacos", que vai representar
os espaços vagos nesse container
2 - Criar 2 classes: Uma chamada Bau e outra chamada Mochila que devem herdar da classe Container.
3 - A classe Bau deve ter o valor do atributo espacos em 30, e a classe Mochila em 10
4 - Criar a classe Item, que tera 2 atributos: Nome e tamanho
5 - Herdando da classe item, você pode herdar um número ilimitado de classes (Espada, Cantil, etc) que terão
que ter a informação de tamanho e nome
6 - Deve ser possível colocar itens dentro de qualquer container, respeitando o espaco maximo do container. Por
exemplo: Se dentro de uma mochila só podem caber itens em que a soma do tamanho não ultrasse 10, não podemos
colocar ao mesmo tempo uma Espada (tamanho: 6), um Cantil (tamanho: 3) e um Mapa (Tamanho: 3)
7 - Antes de colocar um novo item no container, será feita uma verificação da quantidade de espaços disponíveis
nesse container. Se a quantidade máxima de espaços for ultrapassada, deverá ser lançada a exceção de nome
EspacoInsuficiente

"""