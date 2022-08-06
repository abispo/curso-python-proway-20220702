"""
Exercício 01

1 - Criar uma classe chamada Container. Essa classe terá um atributo de nome "espacos", que vai representar
os espaços vagos nesse container
2 - Criar 2 classes: Uma chamada Bau e outra chamada Mochila que devem herdar da classe Container.
3 - A classe Bau deve ter o valor do atributo espacos em 30, e a classe Mochila em 10
4 - Criar a classe Item, que tera 2 atributos: Nome e tamanho
5 - Herdando da classe item, você pode herdar um número ilimitado de classes (Espada, Cantil, etc) que terão
que ter a informação de tamanho e nome
6 - Deve ser possível colocar itens dentro de qualquer container, respeitando o espaco maximo do container. Por
exemplo: Se dentro de uma mochila só podem caber itens em que a soma do tamanho não ultrasse 10, não podemos
colocar ao mesmo tempo uma Espada (tamanho: 6), um Cantil (tamanho: 3) e um Mapa (Tamanho: 3)
7 - Antes de colocar um novo item no container, será feita uma verificação da quantidade de espaços disponíveis
nesse container. Se a quantidade máxima de espaços for ultrapassada, deverá ser lançada a exceção de nome
EspacoInsuficiente

"""


class Container:

    def __init__(self, nome, espacos=5):
        self._nome = nome
        self._espacos = espacos
        self._items = []
        self._espaco_atual = 0

    def adicionar_item(self, item):
        if self._espaco_atual + item.tamanho > self._espacos:
            raise EspacoInsuficiente
        else:
            self._items.append(item)
            self._espaco_atual += item.tamanho

    def info(self):

        espaco_itens = 0
        for item in self._items:
            espaco_itens += item.tamanho

        texto = f"""
        INFORMAÇÕES:
        
        Container: {self._nome}
        Espaço máximo: {self.espacos}
        Itens: {self._items}
        Espaço ocupado: {espaco_itens}
        """

        return texto

    @property
    def espacos(self):
        return self._espacos

    @property
    def nome(self):
        return self._nome

    @espacos.setter
    def espacos(self, novo_valor):
        self._espacos = novo_valor

    @nome.setter
    def nome(self, novo_valor):
        self._nome = novo_valor


class Bau(Container):

    def __init__(self):
        # Chamamos o método __init__ da superclasse para inicializar o atributo _espacos com o valor de 30
        super().__init__(nome="Baú", espacos=30)


class Mochila(Container):

    def __init__(self):
        super().__init__(nome="Mochila", espacos=10)


class Item:

    def __init__(self, nome, tamanho):
        self._nome = nome
        self._tamanho = tamanho

    def __str__(self):
        return f"{self._nome}"

    def __repr__(self):
        return f"{self._nome}"

    @property
    def nome(self):
        return self._nome

    @property
    def tamanho(self):
        return self._tamanho

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self._tamanho = novo_tamanho


class Elmo(Item):
    def __init__(self):
        super().__init__(nome="Elmo", tamanho=4)


class Espada(Item):
    def __init__(self):
        super().__init__(nome="Espada", tamanho=5)


class Cantil(Item):
    def __init__(self):
        super().__init__(nome="Cantil", tamanho=2)


class Mapa(Item):
    def __init__(self):
        super().__init__(nome="Mapa", tamanho=3)


class EspacoInsuficiente(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = "Espaço Insuficiente"

if __name__ == "__main__":
    elmo = Elmo()
    espada = Espada()
    cantil = Cantil()
    mapa = Mapa()

    for item in [elmo, espada, cantil, mapa]:
        print(f"Nome do Item: {item.nome} | Tamanho: {item.tamanho}")

    mochila = Mochila()
    bau = Bau()

    try:
        mochila.adicionar_item(espada)
        mochila.adicionar_item(elmo)
        mochila.adicionar_item(mapa)    # Comente essa linha para não ser lançada a exception

        bau.adicionar_item(elmo)
        bau.adicionar_item(espada)
        bau.adicionar_item(cantil)
        bau.adicionar_item(mapa)

        print(mochila.info())
        print(bau.info())
    except EspacoInsuficiente as exc:
        print(exc.message)
