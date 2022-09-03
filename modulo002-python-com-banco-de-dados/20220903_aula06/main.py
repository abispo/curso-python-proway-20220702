from prog01 import inverte_texto
from prog02 import retorna_info_criptomoeda

if __name__ == "__main__":

    # texto = input("Informe o texto a ser invertido: ")
    # print(inverte_texto(texto))

    criptomoeda = input("Informe a criptomoeda que você deseja obter informações (bitcoin, ethereum): ")
    info_criptomoeda = retorna_info_criptomoeda(criptomoeda)

    print(info_criptomoeda)
