"""
Exercício 2

Criar uma função que receberá 5 notas. A função deve retornar a média aritmética dessas notas. Devem ser
seguidas as seguintes regras:

Deve-se descartar a melhor e a pior nota. A partir das 3 restantes é que se fará a média.
Essa função deve ter um argumento opcional chamado usar_todas_notas, que terá como valor padrão o booleano
False. Se o valor desse argumento for alterado para True, a média deve utilizar as 5 notas.

Devemos utilizar a sintaxe de duplo asterisco para passar os valores para a função

"""


def calculo_nota_final(n1, n2, n3, n4, n5, usar_todas_notas=False):
    pass


if __name__ == '__main__':
    lista_notas = [
        {"n1": 8.5, "n2": 8.5, "n3": 9, "n4": 9.5, "n5": 8},
        {"n1": 7.5, "n2": 6, "n3": 9, "n4": 9.5, "n5": 8, "usar_todas_notas": True},
        {"n1": 9, "n2": 6.5, "n3": 9, "n4": 9.5, "n5": 8, "usar_todas_notas": True},
        {"n1": 9.5, "n2": 9, "n3": 9, "n4": 9.5, "n5": 8},
        {"n1": 9, "n2": 8, "n3": 9, "n4": 9.5, "n5": 8},
    ]