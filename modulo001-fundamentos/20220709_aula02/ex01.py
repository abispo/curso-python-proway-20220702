"""
Exercício

A partir de uma sequência de números, temos que salvar em 2 listas:
* Uma lista com os números positivos
* Uma lista com os números negativos

Utilizar a função range (função geradora)
"""

from random import randint

if __name__ == "__main__":

    # A função range gera números até um limite estabelecido
    lista_pares = []
    lista_impares = []

    for i in range(100):
        numero = randint(0, 1000)

        resultado = numero % 2
        # Se o número for impar, salvar na lista de ímpares
        if resultado == 1:
            lista_impares.append(numero)
        # Se o número for par, salvar na lista de pares
        else:
            lista_pares.append(numero)

        print(f"Lista de pares contém {len(lista_pares)} itens")
        print(f"Lista de ímpares contém {len(lista_impares)} itens")
        # Repete o caractere '-' 50 vezes
        print("-"*50)

    print(lista_pares)
    print(lista_impares)

    # Mostrar qual é a lista com mais números
    # Se houver empate, mostrar que houve empate
    # Dica: Usar a função built-in len()
    if len(lista_pares) > len(lista_impares):
        print("Foram sorteados mais números pares")
    elif len(lista_impares) > len(lista_pares):
        print("Foram sorteados mais números ímpares")
    else:
        print("As listas possuem a mesma quantidade de itens.")
