"""
Orientação a Objetos com Python - Herança

É utilizada quando uma classe herda atributos e métodos de uma outra classe.

"""

import uuid
from random import randint

# Classe base para os pagamentos, não vamos chamá-la diretamente
class Pagamento:

    def __init__(self, valor):
        self._valor = valor

    # Utilizando a exception NotImplementedError, forçamos as classes filhas que precisarem utilizar esse método,
    # a implementarem a sua própria versão do método pagar()
    def pagar(self):
        raise NotImplementedError("Você deve implementar esse método")


class PagamentoPorBoleto(Pagamento):

    def pagar(self):
        texto = f"O boleto de código {uuid.uuid4()} foi gerado com o valor de {self._valor}."
        print(texto)


class PagamentoPorCartaoDeCredito(Pagamento):

    def __init__(self, valor, numero, codigo):
        # A função built-in super() executa um método ou acessa um atributo da superclasse
        super().__init__(valor)
        self._numero = numero
        self._codigo = codigo

    def _tem_limite_disponivel(self):
        return bool(randint(0, 1))

    def pagar(self):
        if self._tem_limite_disponivel():
            texto = f"""
            Dados de pagamento via cartão:
            Valor: {self._valor}
            Número: {self._numero}
            Código: {self._codigo}
            """

            print(texto)
        else:
            print("SEM LIMITE DISPONÍVEL")

    """
    Criar classe chamada PagamentoPorPIX
    Essa classe deve herdar da classe Pagamento
    Antes do pagamento ser realizado, deve-se checar se há saldo disponível
    Os dados de entrada da classe são: Valor a ser pago, agência e número da conta corrente
    """

class PagamentoPorPIX(Pagamento):

    def __init__(self, valor, agencia, conta_corrente):
        super().__init__(valor)
        self._agencia = agencia
        self._conta_corrente = conta_corrente

    def _ha_saldo_disponivel(self):
        return bool(randint(0, 1))

    def pagar(self):
        if self._ha_saldo_disponivel():
            texto = f"""
            Dados de pagamento via PIX:
            Valor: {self._valor}
            Agência: {self._agencia}
            Conta Corrente: {self._conta_corrente}
            """

            print(texto)
        else:
            print("SEM SALDO DISPONÍVEL")

if __name__ == "__main__":
    pagamento_por_boleto = PagamentoPorBoleto(100)
    pagamento_por_boleto.pagar()

    pagamento_por_cartao_de_credito = PagamentoPorCartaoDeCredito(100, "123456", "123")
    pagamento_por_cartao_de_credito.pagar()

    pagamento_por_pix = PagamentoPorPIX(100, "4567", "233567")
    pagamento_por_pix.pagar()
