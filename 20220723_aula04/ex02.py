"""
Criar um arquivo csv que vai agregar as informações dos arquivos .txt criados para o exercício 01
( ex01_a.txt, ex01_b.txt, ex01_c.txt)

Esse novo arquivo .csv terá 4 colunas: nome_aluno, nota_1, nota_2, nota_3
O conteúdo desse arquivo será criado a partir das informações dos arquivos .txt, ou seja, teremos que ler
os 3 arquivos, e pra cada arquivo .txt será criada uma linha no arquivo .csv. Por exemplo:

~conteúdo do arquivo .txt~
Bruna
9.5
8.0
8.5


~conteúdo do arquivo .csv~
nome_aluno;nota_1;nota_2;nota_3
Bruna;9.5;8.0;8.5;

"""
import csv

if __name__ == "__main__":

    # Abrir o arquivo .csv em modo de escrita "w"
    with open("notas.csv", mode="w", encoding="utf-8", newline='') as csv_file:

        # Criar o objeto csv.DictWriter
        fieldnames = ["nome_aluno", "nota_1", "nota_2", "nota_3"]
        arquivo_csv = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

        arquivo_csv.writeheader()

        # Abrir os arquivos .txt
        arquivos_txt = ["ex01_a.txt", "ex01_b.txt", "ex01_c.txt", "ex02_a.txt"]
        for arquivo_txt in arquivos_txt:
            # Abre o arquivo atual do loop
            with open(arquivo_txt, mode="r", encoding="utf-8") as _file:

                # Ler o conteúdo desse arquivo .txt
                conteudo = _file.readlines()

                # Salvar os valores em variáveiss
                nome_aluno = conteudo[0].replace('\n', '')
                nota_1 = float(conteudo[1])
                nota_2 = float(conteudo[2])
                nota_3 = float(conteudo[3])

                # Criar uma nova linha no arquivo .csv com o conteúdo do arquivo .txt
                arquivo_csv.writerow({
                    "nome_aluno": nome_aluno,
                    "nota_1": nota_1,
                    "nota_2": nota_2,
                    "nota_3": nota_3
                })
