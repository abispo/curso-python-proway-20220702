"""
Exercício 03

Escreva um programa que pedirá, via terminal, 10 itens. Esses itens
terão os seguintes campos: Nome, valor, quantidade. Você deverá
armazenar essas informações no formato de dicionário, e você deve
armazenar esses dicionários em uma lista. Exemplo:
lista_de_itens = [
    {"nome": "Fone de ouvido", "quantidade": 100, "valor": 3.90},
    {"nome": "SSD", "quantidade": 8, "valor": 299.90},
]

Pegar essas informações via terminal. Ex:
Informe o nome do Item: Teclado
Informa a quantidade: 40
Informe o valor: 10

A partir dessas informações armazenadas, no final do programa, vamos
mostrar as seguintes informações:
- Quantidade de produtos cadastrados
- Qual o produto com a maior quantidade
- Qual o produto com o maior preço
- Qual foi o maior pedido (quantidade * valor)
- Qual o total de itens pedidos
- Qual o valor total do pedido (soma de quantidade * valor dos itens)
"""

if __name__ == "__main__":

    lista_de_itens = []

    for i in range(10):

        nome_item = input("Informe o nome do item: ")
        quantidade_item = int(input("Informe a quantidade: "))
        valor_item = float(input("Informe o valor: "))

        info = {
            "nome": nome_item,
            "quantidade": quantidade_item,
            "valor": valor_item
        }

        lista_de_itens.append(info)

    print(lista_de_itens)
