"""
Orientação a objetos em Python

"""

# PascalCase    -> Nomes de classes de funções começam sempre com maiúsculas
# camelCase     -> A primeira letra do nome composto deve ser minúscula
# snake_case    -> Todas as letras são minúsculas, e as palavras compostas separadas por _

# Utilizamos a palavra reservada class para criar uma classe
# De preferência, os nomes das classes em Python devem seguir o formato PascalCase. ex:
# Funcionario, FuncionarioTerceirizado, etc
class Pokemon:
    # Em uma classe Python, podemos ter 2 tipos de atributos: de classe e de instância
    # A diferença é que os atributos de instância pertencem a apenas uma instância, enquanto os de classe
    # são compartilhados entre as instâncias.
    # Os atributos de instância são criados dentro do método __init__()

    # O __init__ é considerado o método construtor da classe, ou seja, é o método que é chamado imediatamente
    # após a classe ser instanciada. Ele inicializa os valores dos atributos do objeto
    # self é uma referência ao próprio objeto que está sendo instanciado. Os métodos de uma classe devem
    # obrigatoriamente receber o self como primeiro argumento.
    def __init__(self, name, type, health):
        self._name = name           # Atributos de instância
        self._type = type
        self._health = health

    # O decorator @property altera o comportamento de métodos fazendo-os se comportarem como atributos
    # Decorators são funções que alteram ou extendem o comportamento de outras funções.
    # Vamos utilizar decorators para simular getters e setters como em Java, C#, etc

    # getter do atributo _name
    @property
    def name(self):
        return self._name

    # setter do atributo _name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Os métodos comuns de uma classe devem ser definidos com o self como primeiro argumento
    def attack(self):
        print(f"{self._name} atacou!")

    def dogde(self):
        print(f"{self._name} esquivou!")

    def evolve(self):
        print(f"{self._name} evoluiu!")


if __name__ == "__main__":

    # Aqui instanciamos a classe Pokemon, criando um objeto e passando os valores
    pikachu = Pokemon("Pikachu", "Elétrico", 70)

    # A sintaxe de acesso aos métodos e atributos do objeto é <objeto>.<atributo_ou_metodo()>
    pikachu.attack()

    charizard = Pokemon("Charizard", "Fogo", 200)
    charizard.attack()

    # Quando queremos definir que métodos e atributos dentro de uma classe em Python devem ser tratados como
    # se fossem privados, colocamos um underscore no início do nome.

    # Essa expressão está fora do recomendável, pois estamos alterando o valor de um atributo "privado"
    # diretamente, ao invés de utilizar um método setter
    pikachu.name = "Raichu"

    pikachu.attack()
