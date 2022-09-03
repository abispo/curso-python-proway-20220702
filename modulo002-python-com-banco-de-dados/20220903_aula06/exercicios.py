

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


def ex02(nome_pokemon):
    """
    Exercício 02

    Essa função receberá um nome de pokemon, e vai consultas as informações do pokemon
    Endereço da API: https://pokeapi.co/api/v2/pokemon/{nome_do_pokemon}

    As informações que devem ser retornadas pela função são:
    Experiência base (base_experience)
    Altura (height)
    ID (id)
    Nome (name)
    Peso (weight)

    Essa função deve retornar um dicionário com essas informações

    Deve-se criar um 2 testes unitários: 1 Onde a chamada é feita corretamente, outro onde o usuário passa um nome
    de pokemon que não existe.
    PS: As chamadas para a API devem ser mockadas
    """
