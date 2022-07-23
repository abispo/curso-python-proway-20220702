"""
Exceptions

Uma exception pode ser entendida como um comportamento inesperado do nosso programa, fazendo ele ser finalizado
devido a um erro. Todas as exceptions em Python descendem da classe Exception. Basicamente temos 2 tipos de erros
dentro do Python: Erros de Sintaxe e Erros em Runtime. Erros de Sintaxe são detectados pelo interpretador antes
do programa ser executado, Erros em Runtime acontecem durante a execução do programa.


"""

if __name__ == "__main__":

    # Podemos lançar uma exceção utilizando o comando raise
    # raise Exception("Esse é um erro personalizado.")

    # Para tratar exceções, utilizamos o bloco try...except

    try:
        # Tentando abrir um arquivo que não existe
        open("teste.txt")

    except FileNotFoundError:
        print("Esse arquivo não existe!")

    print("Arquivo finalizado com sucesso")
