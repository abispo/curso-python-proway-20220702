"""
Módulos e pacotes no Python

Um módulo dentro do Python é entendido como uma coleção de funções, classes, variáveis, constantes, etc.
Ou seja, o Python entende que um arquivo .py é um módulo Python. E um módulo dentro do Python pode
ser importado em outros módulos.

Um pacote no Python nada mais é do que uma coleção de módulos. Para indicarmos que uma pasta no projeto
deve ser entendida como um módulo do Python, criamos um arquivo chamado __init__.py dentro desse
pacote.

"""

# Importamos a função 'hello()' do módulo 'prog01'
from prog01 import hello

# Importamos a variável '__version__' do módulo "raiz" do pacote character
from character import __version__

# Quando queremos importar uma função ou um módulo que está dentro de subpacotes, utilizamos a sintaxe
# do ponto (.)
# Chamamos isso também de import absoluto (onde importamos algo a partir do diretório raiz)
from character.base import generate_name

from character.equipment import show_seed

if __name__ == "__main__":
    # Utilizando a função 'hello()' que foi importada do módulo 'prog01'
    print(hello())

    print(f"Versão do módulo character: {__version__}")
    print(generate_name())
    print(show_seed())
