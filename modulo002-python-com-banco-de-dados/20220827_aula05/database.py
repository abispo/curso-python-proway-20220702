# Pacote 'os' da bibliteca padrão do Python. Iremos usar esse pacote
# para ler as variáveis de ambiente do projeto
import os

# O pacote dotenv é utilizado para ler valores de variáveis de ambiente do sistema
from dotenv import load_dotenv

# create_engine é a função utilizada para criar uma conexão com o banco de dados
from sqlalchemy import create_engine

# declarative_base serve para utilizarmos uma classe base como modelo para as nossas
# classes mapeadas
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker cria a sessão de acesso ao banco de dados
from sqlalchemy.orm import sessionmaker

# Carrega as informações do arquivo .env e define as variáveis de ambiente
load_dotenv()

# Lendo os valores das variáveis de ambiente e salvando em variáveis
db_user = os.getenv("DATABASE_USER")
db_pass = os.getenv("DATABASE_PASSWORD")
db_host = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT")
db_name = os.getenv("DATABASE_NAME")

# Definimos a connection string, que é a string de conexão ao banco de dados.
connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# create_engine retorna um objeto engine, que é responsável por estabelecer a conexão
# com o banco de dados
# O parâmetro echo=True imprime no terminal todos os comandos SQL executados
engine = create_engine(connection_string, echo=True)

# declarative_base retorna a classe base a qual todas as classes do nosso projeto, que forem
# models, irão herdar. Precisamos fazer isso para ser possível mapear as classes para
# as tabelas no banco de dados.
Base = declarative_base()

# Criamos a sessão. É por meio desse objeto que o SQLAlchemy executa as instruções SQL
# no banco de dados
Session = sessionmaker(bind=engine)
session = Session()
