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

    # O comando try captura uma exceção dentro do bloco de código
    try:
        # Tentando abrir um arquivo que não existe

        # O comando assert faz uma comparação entre 2 expressões, lançando uma exceção caso essa comparação
        # retorne False
        assert 1 == 0

        open("teste.txt")

    # O except captura essa exceção que foi identificada dentro do bloco try, possibilitando ao dev
    # tratá-la
    # No caso abaixo, se a exceção capturada for do tipo FileNotFoundError, uma mensagem é mostrada
    # except (FileNotFoundError):
    #     print("Esse arquivo não existe!")

    # except AssertionError:
    #     print("Essa comparação é inválida")

    except Exception:
        print("Erro!")

    print("Arquivo finalizado com sucesso")
