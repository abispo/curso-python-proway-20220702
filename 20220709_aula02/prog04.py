"""
Dicionários
    - São estruturas de dados em formato chave: valor, que podem
    armazenar qualquer tipo de dado (inclusive outros dicionários)
    - Indexáveis
    - Mutáveis
    - Iteráveis
"""

if __name__ == "__main__":

    # Criando um dicionário
    info = {}
    info = {
        "nome": "Curso de Python",
        "turma": "20220702",
        "módulo": "Fundamentos",
        "notas": [5, 6, 6],
        "mais_info": {
            "obs": ""
        },
        5: 1,
        4.5: 12,
    }

    print(info)

    info = dict()
    info = dict(
        nome="Curso de Python",
        turma="20220702",
        modulo="Fundamentos",
        notas=[5, 6, 7],
        mais_info=dict(obs="")
    )

    print(info)

    # Dicionários são indexáveis. Indicamos o nome da chave para
    # acessarmos o seu valor
    print(info["turma"])
    info["turma"] = "20220802"
    # O método get() retorna o valor associado a chave. Se essa chave
    # não existir, ele retorna o valor None (nulo). Podemos definir
    # também um valor padrão que será retornado caso essa chave
    # não exista.
    print(info.get("batata", "A chave batata não existe"))
    print(info["turma"])

    # Dicionários são mutáveis, conseguimos adicionar ou remover
    # chaves e alterar os valores associados a essas chaves
    # A chave localizacao não existe, e será criada
    info["localizacao"] = "Blumenau"
    print(info)

    # O método setdefault() retorna o valor associado à chave. Se
    # essa chave não existir, ele a cria e retorna o valor associado
    print(info.setdefault("sala", "black"))
    print(info)

    # O método update() atualiza o par chave-valor do dicionário.
    # Se a chave não existir, ele cria.
    info.update({"sala": "yellow", "periodo": "Agosto"})
    print(info)

    # Os dicionários são iteráveis, ou seja, podemos processar
    # um dicionário em um laço for

    print("="*50)

    # Por padrão, em um laço for, são retornadas as chaves desse
    # dicionário. Também podemos explicitar o retorno das chaves
    # utilizando o método .keys()
    for item in info.keys():
        print(item)

    # O método values() retorna os valores do dicionário
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

    # O método items() retorna uma lista de tuplas com as chaves
    # e os valores

    # Removendo itens (chave-valor) de um dicionário

    # O método pop() remove um par chave:valor a partir do nome
    # da chave
    info.pop("periodo")
    print(info)

    # O método popitem() remove o último par chave:valor inserido
    info.popitem()
    print(info)

    # Também podemos utilizar a palavra reservada del
    del info["localizacao"]
    print(info)

    # "Limpamos" o dicionário
    info.clear()
    print(info)
