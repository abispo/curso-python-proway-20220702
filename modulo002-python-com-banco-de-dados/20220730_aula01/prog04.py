"""
Orientação a Objetos com Python - Composição

Composição: Quando um objeto é composto por 1 ou mais objetos

Implementando um baralho com a opção de embaralhar
Vamos criar 2 classes: A classe Baralho, e a classe Carta
Um baralho é composto de várias cartas

Existem 4 naipes: Copas, Ouros, Paus, Espadas
Existem 13 valores de cartas: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

"""

import random

NAIPES = ["\u2660", "\u2665", "\u2663", "\u2666"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Baralho:
    def __init__(self):
        self._cartas = []

        for naipe in NAIPES:
            for valor in VALORES:
                self._cartas.append(Carta(valor=valor, naipe=naipe))

    def embaralhar(self):
        random.shuffle(self._cartas)


class Carta:
    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    # O método mágico __str__ altera o comportamento padrão da classe quando ela é passada como argumento
    # para a função built-in str()
    # Ao invés de retornar o objeto e a sua posição na memória, será retornado o naipe e o valor da carta
    def __str__(self):
        return f"{self._naipe}{self._valor}"

    # O método mágico __repr__ altera o formato de exibição da classe quando ela está dentro de um
    # container (lista, tupla, etc)
    def __repr__(self):
        return f"{self._naipe}{self._valor}"


if __name__ == "__main__":

    baralho = Baralho()
    baralho.embaralhar()
    print(baralho._cartas)
