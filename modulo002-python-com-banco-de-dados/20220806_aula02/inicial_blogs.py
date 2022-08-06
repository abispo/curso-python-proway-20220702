
import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect("db.sqlite3")

    sql = """
    CREATE TABLE IF NOT EXISTS tb_usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    """

    conn.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS tb_perfis(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)
    )
    """

    conn.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    texto TEXT NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES tb_usuarios(id)
    )
    """

    conn.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS tb_comentarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_postagem INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    texto TEXT NOT NULL,
    FOREIGN KEY(id_postagem) REFERENCES tb_postagens(id),
    FOREIGN KEY(id_usuario) REFERENCES tb_usuarios(id)
    )
    """

    conn.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS tb_categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL)
    """

    conn.execute(sql)

    # Tabela associativa da relação N:N das tabelas tb_categorias e tb_postagens
    sql = """
    CREATE TABLE IF NOT EXISTS tb_categorias_postagens(
    id_categoria INTEGER NOT NULL,
    id_postagem INTEGER NOT NULL,
    PRIMARY KEY(id_categoria, id_postagem),
    FOREIGN KEY(id_categoria) REFERENCES tb_categorias(id),
    FOREIGN KEY(id_postagem) REFERENCES tb_postagens(id)
    )
    """

    conn.execute(sql)
