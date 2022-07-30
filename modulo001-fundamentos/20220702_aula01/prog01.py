# Entrada e saída via terminal

"""
Utilizamos 2 funções built-in do Python quando queremos mostrar e ler informações
do terminal

print()  -> Imprime uma mensagem na tela
   - Recebe uma expressão válida do Python e retorna para o terminal
input()  -> Recebe uma informação pelo teclado
   - Os dados capturados pelo teclado são entendidos como do tipo string (str)

"""

# string multi-linha
"""
: (dois pontos) -> Novo bloco de código
Cada bloco de código precisa ter uma identação de 4 caracteres

"""

if __name__ == "__main__":
    pass  # Ignora essa linha (Isso é um comentário)

    print("Bem-vindo ao curso de Python")
    # Python é uma linguagem dinamicamente tipada, ou seja, não precisamos
    # definir o tipo de uma variável no momento de sua criação
    # O Python altera o tipo da variável de forma automática, se um novo
    # valor for atribuído a ela
    soma = 2 + 2
    print(soma)

    # = -> Operador de atribuição
    idade = int(input("Informe a sua idade: "))

    # Precisamos converter o valor da variável idade para um tipo numérico
    # Ou fazemos idade = int(idade)
    # Ou fazemos idade = int(input("Informe a sua idade: "))

    # Podemos "montar" uma string de 2 maneiras:
    # Utilizando o método format()
    # Utilizando f-strings

    print("Sua idade é {}".format(idade))
    nova_idade = 10 + idade
    # Dentro das chaves podemos colocar qualquer expressão válida
    print(f"Sua nova idade é {nova_idade}")
