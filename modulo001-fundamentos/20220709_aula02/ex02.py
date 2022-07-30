"""
Exercício 2

Dada uma sequência randômica de letras e números, criar um programa
que consiga diferenciar essas letras e números, com as regras a
seguir:

    * Ao final do programa, mostrar uma lista com os números que fazem parte dessa string
        * Mostrar também a soma desses números
    * Mostrar uma lista com as letras que fazem parte dessa string
        * Entre essas letras, mostrar quais são vogais e quais são consoantes

    Ex: he7sq90nb2k
    Lista de números: [7, 9, 0, 2]  dica: utilizar a função built-in sum()
    Soma dos números: 18
    Lista de letras: ['h', 'e', 's', 'q', 'n', 'b', 'k']
    Vogais: ['e']
    Consoantes: ['h', 's', 'q', 'n', 'b', 'k']

    lista_de_vogais = ['a', 'e', 'i', 'o', 'u']

    Dicas
        - Utilizar função de string isdigit()

"""

from random import choices
from string import ascii_lowercase, digits

if __name__ == "__main__":

    # O método de string join() justa uma lista de itens em uma string, separando pelo caractere
    # definido
    string_randomica = ''.join(choices(f"{ascii_lowercase}{digits}", k=50))
    vogais = "aeiou"

    print(f"String randômica: {string_randomica}")

    lista_numeros = []
    lista_letras = []
    lista_vogais = []
    lista_consoantes = []

    for caractere in string_randomica:

        if caractere.isdigit():
            lista_numeros.append(int(caractere))
        else:
            lista_letras.append(caractere)
            if caractere in vogais:
                lista_vogais.append(caractere)
            else:
                lista_consoantes.append(caractere)

    print(f"Lista de números: {lista_numeros}")
    print(f"Soma dos números: {sum(lista_numeros)}")
    print(f"Lista das letras: {lista_letras}")
    print(f"Lista de vogais: {lista_vogais}")
    print(f"Lista de consoantes: {lista_consoantes}")
