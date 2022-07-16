"""
Funções

Funções (ou procedures) são trechos de código que podem ser definidos em determinados lugares do nosso
código e chamados em quaisquer outros lugares. São trechos de código que são reutilizáveis.

Funções em Python possuem um nome, podem ou não receber parâmetros (ou argumentos) e podem retornar
explicitamente um valor.

Utilizamos a palavra reservada 'def' para criar uma função. O corpo de uma função é um bloco de código.

"""


# Uma função em Python pode ter apenas o seu corpo, sem receber nenhum argumento
def hello():
    return "Hello world"


# palavra é o nome do argumento que vamos passar para a função
def inverte_palavra(palavra):
    # O comando return faz a função retornar o valor que está sendo especificado
    # Se uma função não tem o comando return, ela retorna um valor None por padrão
    return palavra[::-1]


# Podemos também ter argumentos com valores padrão. Nesse caso, não somos obrigados a passar um valor
# para o argumento quando vamos chamar a função
def repetir_palavra(palavra, vezes=1):
    return palavra * vezes


# Podemos criar funções que recebem uma quantidade indefinida de argumentos. Nesse caso fazemos o caminho
# contrário, "empacotamos" os valores passados para a função em 1 argumento apenas. Geralmente indicamos
# esses argumentos com o nome de *args ou **kwargs
def ordenar_numeros(*args):
    return sorted(args)


# Podemos também passar um dicionário com qualquer quantidade de pares chave-valor para a função.
# Dessa maneira precisamos utilizar a sintaxe de 2 arteriscos
def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


if __name__ == '__main__':

    print(hello())

    # Chamamos a função passando um parâmetro
    inverte_palavra("Python")

    # Passando o retorno da função inverte_palavra para a função built-in print()
    print(inverte_palavra("Curso de Python"))

    # Como não passamos um valor para o argumento "vezes", será usado o valor padrão (1)
    print(repetir_palavra("Python"))

    # Dessa vez passamos o valor 5 para o argumento vezes
    print(repetir_palavra("Golang", 5))

    # Podemos também passar os valores para as funções indicando a qual argumento esses valores
    # serão atribuídos. Podemos chamar isso de passagem de valores via keyword (palavra-chave)
    print(repetir_palavra(vezes=10, palavra="PHP"))

    # Também podemos passar os valores para a função utilizando os argumentos de forma arbitrária.
    # Podemos chamar isso também de unpacking (desempacotamento) de valores
    valores = ["C++", 6]

    # A quantidade de itens na lista deve ser igual a quantidade de argumentos obrigatórios na função
    print(repetir_palavra(valores[0], valores[1]))

    # Utilizando o unpacking (*)
    print(repetir_palavra(*valores))

    valores = {
        "palavra": "Rust",
        "vezes": 3
    }

    # Desempacotando os valores de um dicionário na chamada da função
    # ATENÇÃO: Os nomes das chaves do dicionário devem ser exatamente iguais aos nomes dos argumentos
    print(repetir_palavra(**valores))

    # *args
    print(ordenar_numeros(5, 8, 2, 7, 9))
    print(ordenar_numeros(3, 5))

    # **kwargs
    mostrar_info(nome="Amanda", idade=18)
    mostrar_info(nome="Estela", idade=29, sexo="F", estado="RJ")
