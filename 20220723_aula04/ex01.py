"""
Ler o conteúdo dos arquivos ex01_a.txt. ex01_b.txt, ex01_c.txt.
Esses arquivos contém o nome e as notas de um aluno

Ler esse arquivo, calcular a média do aluno utilizando essas 3 notas e mostrar no final se:
* A média for menor do que 5, o aluno estará reprovado
* Se a média for maior ou igual a 5 e menor do que 7, mostrar que ele está de recuperação
* Se a média for maior ou igual a 7, mostrar que ele foi aprovado

Exemplo de saída:

O aluno João foi aprovado com a média 10 (10, 10, 10)
O aluno Carlos está de recuperação com a média 6.5 (6.5, 6.5, 6.5)
O aluno José foi reprovado com a média 4 (4, 4, 4)

Dica: Se precisar substituir ou remover um caractere, utilize o método de string replace()

"Pcthon".replace("c", "y")  -> "Python"

:.2f

"""


if __name__ == "__main__":

    arquivos = ["ex01_a.txt", "ex01_b.txt", "ex01_c.txt"]

    for arquivo_item in arquivos:
        # Abre o arquivo atual do loop
        with open(arquivo_item, mode="r", encoding="utf-8") as _file:
            # Lê o conteúdo do arquivo
            conteudo = _file.readlines()

            nome_aluno = conteudo[0].replace('\n', '')
            nota_1 = float(conteudo[1])
            nota_2 = float(conteudo[2])
            nota_3 = float(conteudo[3])
            estado = ""

            # Faz os cálculos
            media = (nota_1 + nota_2 + nota_3) / 3

            if media < 5:
                estado = "reprovado"

            elif media >= 5 and media < 7:
                estado = "em recuperação"

            else:
                estado = "aprovado"

            # Imprime o resultado
            print(f"O aluno {nome_aluno} está {estado} com a média {media:.1f} ({nota_1}, {nota_2}, {nota_3}).")
