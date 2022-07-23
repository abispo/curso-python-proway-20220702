"""
Trabalhando com arquivos .csv (Comma Separated Values | Valores Separados por vírgula)

Utilizando as classes DictReader e DictWriter

"""
import csv
import uuid
import random

if __name__ == "__main__":

    with open("prog03.csv", mode="a", encoding="utf-8", newline='') as _file:

        arquivo_csv = csv.DictWriter(_file, fieldnames=["id", "nome", "score"], delimiter=';')

        # O método writeheader() escreve no arquivo o nome das colunas
        # Antes de escrever o cabeçalho, verificamos se já existe conteúdo no arquivo.
        # Se não existir (posição do cursor em 0), criamos o cabeçalho
        if _file.tell() == 0:
            arquivo_csv.writeheader()

        # O método writerow() escreve uma linha no arquivo csv
        # Diferentemente do método writerow() do objeto csv.writer, o método writerow() do objeto csv.DictWriter
        # recebe um dicionário ao invés de uma lista
        arquivo_csv.writerow({
            "id": str(uuid.uuid4()),            # Gera um ID randômico (letras e números separados por hífen)
            "nome": "Vanessa",
            "score": random.randint(400, 1000)  # Gera um número inteiro entre 400 e 1000
        })

        # O método writerows escreve várias linhas no arquivo csv (listas de dicionários)
        arquivo_csv.writerows([
            {"id": str(uuid.uuid4()), "nome": "Wilma", "score": random.randint(400, 1000)},
            {"id": str(uuid.uuid4()), "nome": "Lais", "score": random.randint(400, 1000)}
        ])
