"""
Orientação a Objetos com Python - Encapsulamento

Utiliza a abstração como base, porém trabalha mais a nível de aplicação. É o processo onde “protegemos”
determinadas propriedades ou métodos de serem “expostos”.

A máquina de café terá que armazenar café, água, açúcar, leite e chocolate. O usuário poderá escolher
a bebida que quiser escolhendo uma das opções que serão mostradas, que são:
    1) Café (Café + água)
    2) Cappuccino (Café + água + chocolate)
    3) Leite (Leite + água)
    4) Chocolate (Chocolate + água)

Os ingredientes estarão armazenados na máquina

"""


class MaquinaDeCafe:

    def __init__(self, cafe=5000, leite=2000, chocolate=2000):
        self._cafe = cafe
        self._leite = leite
        self._chocolate = chocolate

    def preparar_bebida(self, opcao):
        if opcao == 1:
            self._fazer_cafe()
        elif opcao == 2:
            self._fazer_cappuccino()
        elif opcao == 3:
            self._fazer_leite()
        elif opcao == 4:
            self._fazer_chocolate()
        else:
            print("OPÇÃO DESCONHECIDA")

    def _fazer_cafe(self):
        print("PREPARANDO O CAFÉ")
        self._esquentar_a_agua()
        self._misturar()

    def _esquentar_a_agua(self):
        print("ESQUENTANDO A ÁGUA")

    def _misturar(self):
        print("MISTURANDO INGREDIENTES")

    def _fazer_cappuccino(self):
        pass

    def _fazer_leite(self):
        pass

    def _fazer_chocolate(self):
        pass


if __name__ == "__main__":

    texto = """
    Escolha a sua bebida:
    
    1) Café (Café + água)
    2) Cappuccino (Café + água + chocolate)
    3) Leite (Leite + água)
    4) Chocolate (Chocolate + água)
    """

    print(texto)

    opcao = int(input("Informe a opção escolhida: "))

    maquina_de_cafe = MaquinaDeCafe()
    maquina_de_cafe.preparar_bebida(opcao)