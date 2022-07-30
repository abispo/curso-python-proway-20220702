
# Utilizando a constante SEED do módulo base, fazendo o import absoluto
#from character.base import SEED

# Utilizando a constante SEED do módulo base, fazendo o import relativo
# O ponto (.) significa que estamos referenciando o módulo base que está no mesmo pacote em relação ao
# módulo equipment
from .base import SEED


def show_seed():
    return SEED
