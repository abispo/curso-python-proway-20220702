"""
Exceptions

Uma exception pode ser entendida como um comportamento inesperado do nosso programa, fazendo ele ser finalizado
devido a um erro. Todas as exceptions em Python descendem da classe Exception. Basicamente temos 2 tipos de erros
dentro do Python: Erros de Sintaxe e Erros em Runtime. Erros de Sintaxe são detectados pelo interpretador antes
do programa ser executado, Erros em Runtime acontecem durante a execução do programa.

"""


# Podemos também criar classes de exceção personalizadas, que devem obrigatoriamente
# herdar da classe base Exception
class SenhaIncorretaError(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.mensagem = "Senha incorreta!"


if __name__ == "__main__":

    try:
        senha = "456"

        if senha != "456":
            print("Verificando senha...")
            # A palavra reservada raise serve para "lançar" uma exceção. Ou seja, se esse comando estiver dentro
            # de um bloco try... except, a exceção lançada será capturada
            raise SenhaIncorretaError("Senha incorreta!")

    # Aqui capturamos a nossa exception personalizada
    except SenhaIncorretaError as exc:
        print(exc.mensagem)

    # O bloco else só é executado se nenhuma exception for lançada(capturada)
    else:
        print("Nenhum erro encontrado!")

    # O bloco finally sempre será executado, independentemente se alguma exceção foi lançada ou não
    finally:
        print("Verificação de senha finalizada.")
