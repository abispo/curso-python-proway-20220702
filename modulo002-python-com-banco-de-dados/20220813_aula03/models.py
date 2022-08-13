"""
Nesse módulo ficarão todas as classes que serão mapeadas para tabelas no banco de dados

"""

# Importando a classe Base
from database import Base

# Importando as classes do SQLAlchemy que representam os tipos de dados da tabela
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

"""
O SQLAlchemy irá ler a estrutura dessa classe, e vai gerar um comando SQL CREATE TABLE, com
a estrutura similar a abaixo:

CREATE TABLE IF NOT EXISTS tb_users(
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL
)
"""
class User(Base):

    # __tablename__ permite definir o nome da tabela mapeada no banco de dados
    __tablename__ = "tb_users"

    # Os atributos abaixo serão os nomes e os tipos das colunas na tabela tb_users:
    # id será um campo do tipo integer, chave primária e auto incremento
    # email e password serão campos do tipo varchar, de tamanho 200 e que não
    # aceitam valores nulos
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    # O atributo profile não será criado na tabela. Ele é uma espécie de "atributo virtual",
    # que só irá existir na execução do código. Ele serve pra referenciar o objeto
    # que está relacionado
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    posts = relationship("Post", back_populated="user")

    def __repr__(self):
        return f"<User({self.id}, {self.email})>"

    __str__ = __repr__


class UserProfile(Base):

    __tablename__ = "tb_users_profiles"

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)

    # Como primeiro argumento, passamos a model que está relacionada
    # Como segundo argumento, passamos o nome do campo de ligação da tabela relacionada
    # Como terceiro argumento, passamos uselist=False para o retorno ser um objeto, e não uma lista
    user = relationship("User", back_populates="profile", uselist=False)

    def __repr__(self):
        return f"<UserProfile({self.id}, {self.first_name}, {self.last_name})>"

    __str__ = __repr__

"""
Criar a model Post, com os seguintes atributos
    o nome da tabela no banco de dados deve ser tb_posts
    id  integer     primary key     auto increment
    user_id     integer foreign key not null
    title       varchar(100) not null
    content     TEXT
    criar o campo user que será do tipo relationship
    na model User, criar o campo posts que vai ser do tipo relationship, e deve retornar uma lista
"""

class Post(Base):

    __tablename__ = "tb_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("tb_users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

    user = relationship("User", back_populates="posts", uselist=False)

    def __repr__(self):
        return f"<Post({self.id}, {self.title})>"

    __str__ = __repr__