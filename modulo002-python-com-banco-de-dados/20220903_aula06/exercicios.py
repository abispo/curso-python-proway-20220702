

def ex01(texto):
    """
    Exercício 01

    Escreva uma função que receba um texto qualquer, e organize as letras desse texto em order alfabética. Escreva
    também 2 testes unitários para essa função: Um teste que retorne exatamente a string em ordem alfabética (caminho
    feliz) e outro teste que capture a exceção caso o usuário passe um valor diferente de string para a função

    Crie o módulo tests/test_exercicios.py
    Crie a classe TestExercicios que conterá os testes unitários dos exercícios
    Dica: Converta a string para uma lista antes de ordenar as letras por ordem alfabética
    Dica 2: Converta novamente essa lista para a string já com a ordenação
    """

    if isinstance(texto, str):
        lista_letras = list(texto)
        lista_letras.sort()
        return "".join(lista_letras)

    raise Exception("Você deve passar um tipo string para a função")
