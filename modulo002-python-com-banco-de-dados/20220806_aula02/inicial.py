"""
Arquivo inicial

Nesse arquivo vamos configurar a nossa base de dados, inserir registros, ETC

"""

import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect("db.sqlite3")

    # Criar uma nova tabela
    comando = """
    CREATE TABLE IF NOT EXISTS tb_usuarios1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """

    conn.execute(comando)

    # Inserir valores na tabela
    comando = """
    INSERT INTO tb_usuarios1(nome) VALUES ('Maria')
    """

    conn.execute(comando)
    conn.commit()

    comando = """
    UPDATE tb_usuarios1 SET nome = 'Joana' WHERE id = 1
    """
    conn.execute(comando)
    conn.commit()

    comando = """
    SELECT * FROM tb_usuarios1
    """

    cursor = conn.execute(comando)

    for linha in cursor:
        print(f"ID: {linha[0]}, Nome: {linha[1]}")

    comando = "DELETE FROM tb_usuarios1"
    conn.execute(comando)
    conn.commit()

    comando = "DROP TABLE tb_usuarios1"
    conn.execute(comando)
