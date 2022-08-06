"""
Exercício 01

Ler os registros do arquivo alunos.csv e salvar na tabela tb_alunos


"""

import sqlite3
import csv

if __name__ == "__main__":

    # Criar a conexão com o banco
    conn = sqlite3.connect("db.sqlite3")

    # Criar a tabela tb_alunos
    sql = """
    CREATE TABLE IF NOT EXISTS tb_alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    n1 REAL NOT NULL,
    n2 REAL NOT NULL,
    n3 REAL NOT NULL
    )
    """

    conn.execute(sql)

    with open(file="alunos.csv", mode="r", encoding="utf-8") as _file:

        fieldnames = ["nome", "n1", "n2", "n3"]
        csv_reader = csv.DictReader(_file, fieldnames=fieldnames, delimiter=';')

        # A função built-in enumerate() retorna um índice junto com a sequência a ser lida
        for indice, item in enumerate(csv_reader):
            if indice > 0:
                sql = f"""
                INSERT INTO tb_alunos(nome, n1, n2, n3)
                VALUES (
                    "{item['nome']}", {float(item['n1'])}, {float(item['n2'])}, {float(item['n3'])}
                ) 
                """
                conn.execute(sql)
                conn.commit()