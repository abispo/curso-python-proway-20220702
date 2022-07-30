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

    produto_com_maior_quantidade = {
        "nome": "", "quantidade": 0, "valor": 0
    }

    produto_com_maior_preco = {
        "nome": "", "quantidade": 0, "valor": 0
    }

    produto_com_maior_valor = {
        "nome": "", "valor": 0
    }

    total_de_itens_pedidos = 0
    total_geral = 0

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

        # Verificar se esse item tem uma quantidade unitária maior que o anterior(registrado)
        if info.get("quantidade") > produto_com_maior_quantidade.get("quantidade"):
            produto_com_maior_quantidade.update(info)

        # Verificar se esse item tem um preço unitário maior que o anterior(registrado)
        if info.get("valor") > produto_com_maior_preco.get("valor"):
            produto_com_maior_preco.update(info)

        # Vericar se a quantidade * valor desse item é maior que o registrado.
        # valor_atual = info.get("quantidade") * info.get("valor")
        if (info.get("quantidade") * info.get("valor")) > produto_com_maior_valor.get("valor"):
            produto_com_maior_valor.update({
                "nome": info.get("nome"),
                "valor": info.get("quantidade") * info.get("valor")
            })

        # total_de_itens_pedidos += info.get("quantidade")
        total_de_itens_pedidos = total_de_itens_pedidos + info.get("quantidade")

        total_geral = total_geral + (info.get("quantidade") * info.get("valor"))

        print("-"*20)

    print(f"Quantidade de itens cadastrados: {len(lista_de_itens)}")
    print(
        f"Produto com maior quantidade: "
        f"{produto_com_maior_quantidade.get('nome')}"
        f" ({produto_com_maior_quantidade.get('quantidade')})"
    )

    print(
        f"Produto com maior preço: "
        f"{produto_com_maior_preco.get('nome')}"
        f" ({produto_com_maior_preco.get('valor')})"
    )

    print(
        f"Qual foi o maior pedido: "
        f"{produto_com_maior_valor.get('nome')}"
        f" ({produto_com_maior_valor.get('valor')})"
    )

    print(f"Quantidade total de itens: {total_de_itens_pedidos}")

    print(f"Total geral: {total_geral}")
