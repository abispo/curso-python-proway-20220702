"""
Exercício

Crie uma função que receba uma quantidade indefinida de argumentos (que serão números). Essa função
deve retornar uma tupla: O primeiro valor dessa tupla deve ser o maior número, e o segundo valor
dessa tupla deve ser o menor número. Exemplo:

maior, menor = maior_e_menor(4, 7, 3, 9, 6)

print(maior)    # Deve imprimir 9
print(menor)    # Deve imprimir 3

Na função, podemos retornar mais de 1 valor ao mesmo tempo. Exemplo:
return 1, 20

Dica: Utilize as funções built-in max() e min()

"""


def maior_e_menor(*args):
    maior = max(args)
    menor = min(args)

    return maior, menor


if __name__ == '__main__':
    maior, menor = maior_e_menor(45, 2, 7, 89, 12, 32, 84, 19)
    print(maior)
    print(menor)
