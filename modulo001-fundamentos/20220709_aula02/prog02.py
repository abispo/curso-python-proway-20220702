"""
Listas
    - São estruturas de dados que podem também ser chamadas de
    containeres (estruturas que armazenam outros dados). Listas são:
    - Ordenáveis
    - Mutáveis
    - Iteráveis
    - Indexáveis
    - Listas são heterogêneas. Podem armazenar diversos tipos de
    dados, inclusive outras listas.

"""

if __name__ == '__main__':

    # Sintaxe de criação de listas
    carros = ["Gol", "Marea", "Parati"]

    print(carros)

    # Inserindo um novo carro no final da lista
    carros.append("Vectra")
    print(carros)

    # Inserindo um novo carro no índice 2 da lista
    carros.insert(2, "Kombi")
    print(carros)

    # O índice de uma lista sempre começa pelo 0
    """
    carros = ['Gol', 'Marea', 'Kombi', 'Parati', 'Vectra']
    índices     0       1       2           3        4
    ind. neg.   -5      -4      -3          -2       -1
    """

    # Como listas são indexáveis, conseguimos acessar um determinado
    # item a partir do seu índice
    print(carros[2])

    # Podemos também utilizar índices negativos
    print(carros[-2])

    # O Python também nos permite "fatiar" listas, definindo um índice de início, um de fim
    # e um "step", ou seja, de quantos em quantos itens. Damos a isso o nome de slicing

    # Isso é uma list comprehension (Uma maneira mais "enxuta" de criar listas)
    lista = [numero for numero in range(1000)]
    # Gera uma nova lista começando do índice 100 até o índice 119, pulando de 2 em 2
    nova_lista = lista[100:120:2]
    print(nova_lista)

    # Gera uma nova lista começando do índice 0 até o índice 19, pulando de 1 em 1
    nova_lista = lista[:20]
    print(nova_lista)

    # Gera uma nova lista começando do índice 500 até o índice lista[-1] (último), pulando de 1 em 1
    nova_lista = lista[500:]
    print(nova_lista)

    # Gera uma nova cópia da lista
    nova_lista = lista[:]
    print(nova_lista)

    """
    lista[i:f:s]
    i -> Índice inicial
    f -> Índice final
    s -> step (de quantos em quantos)
    
    Esses parâmetros não são obrigatórios:
    - Se omitirmos o índice inicial, será gerada uma lista começando do índice 0 até o f
    - Se omitirmos o índice final, será gerada uma lista começando do índice i até lista[-1]
    - Se omitirmos o step, serão gerados os itens em sequência de 1
    
    Detalhe: O índice final é exclusivo, ou seja, ele não é retornado. Ao invés
    disso, o item retornado é o índice final - 1
    """

    # Copiando listas
    a = 5
    b = a
    b = 4
    print(a, b)

    lista_de_compras1 = ["Sabão", "Banana", "Tomate"]
    lista_de_compras2 = lista_de_compras1
    lista_de_compras2.append("Batata")

    # Alteramos de forma indireta os valores de lista_de_compras_1, pois indicamos que
    # lista_de_compras2 precisa apontar para a mesma posição de memória que lista_de_compras1.
    # Essa é a maneira incorreta de copiar os valores de uma lista para a outra
    print(lista_de_compras1)
    print(lista_de_compras2)

    # Maneira correta de copiar os valores de uma lista em outra
    lista_de_compras2 = lista_de_compras1.copy()
    lista_de_compras3 = lista_de_compras1[:]
    pass
