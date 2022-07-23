"""
Trabalhando com arquivos .csv (Comma Separated Values | Valores Separados por vírgula)

Arquivos csv são arquivo texto comuns, porém com algumas marcações especiais. Geralmente, um arquivo CSV possui
uma linha que representa os cabeçalhos (ou títulos das colunas) e os valores. Exemplo:

id;nome;score
1;Bruna;800
2;Patricia;850
3;Elza;900

No exemplo acima, a primeira linha representa os títulos das colunas, as linhas 2, 3, 4 representam os valores
de cada coluna, e o caractere ';' é o caractere separador.

Utilizamos o módulo csv pra trabalhar com esses arquivos dentro do Python.

"""

import csv


if __name__ == "__main__":

    # Primeiro abrimos o arquivo de forma comum
    # O argumento newline altera o caractere que será utilizado pra quebra de linha
    with open("prog02.csv", mode="w", encoding="utf-8", newline='') as _file:

        # Criamos o objeto arquivo CSV a partir do objeto arquivo que abrimos utilizando o open()
        # Podemos mudar o caractere separador padrão utilizando o argumento delimiter
        arquivo_csv = csv.writer(_file, delimiter=';')

        """
        Podemos escrever no arquivo .csv de 2 formas: Utilizando os métodos writerow() ou writerows()
        """

        # O método writerow() recebe uma lista com os valores que serão escritos no arquivo.
        # Como estamos trabalhando com um arquivo CSV, esses valores serão separados de forma automática
        arquivo_csv.writerow(["Jaqueline", 29, "SC"])
        arquivo_csv.writerow(["Thays", 30, "SP"])

        # Utilizando o método writerows, precisamos passar uma lista de listas, cada lista representando
        # uma nova linha
        arquivo_csv.writerows([
            ["Viviane", 19, "PE"], ["Fátima", 18, "SP"], ["Luíza", 25, "ES"]
        ])

    with open("prog02.csv", mode='r', encoding="utf-8") as _file:

        # Nesse caso, precisamos passar o argumento delimiter=';', pois o módulo CSV não vai entender esse caractere
        # como delimitador, pois leva por padrão o caractere ','
        arquivo_csv = csv.reader(_file, delimiter=';')

        for linha in arquivo_csv:
            print(linha)
