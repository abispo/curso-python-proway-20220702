
MODULO 3 - Python WEB

Instalando o Django:
    pip install django
    ou instalamos pela aba Packages do PyCharm

Comando para criação do projeto em Django
    django-admin.exe startproject mysite .
    O ponto no final vai criar os arquivos do projeto no mesmo diretório onde o usuário digitou o comando. Se o ponto no final for omitido,
    Será criada uma pasta chamada mysite, e dentro dessa pasta serão criados os arquivos do projeto

Estrutura de arquivos do projeto
    Quando o projeto é criado, a seguinte estrutura de arquivos é criada:
        mysite/
            - __init__.py
            - asgi.py
            - settings.py
            - urls.py
            - wsgi.py
        manage.py

    - __init__.py         -> É um arquivo que indica que essa pasta é um módulo do Python
    - asgi.py, wsgi.py    -> São arquivos que utilizamos na fase de deploy (publicação) da aplicação. Basicamente é por eles que o projeto
    será executado em produção.
    - settings.py         -> É o arquivo de configurações globais da aplicação.
    - urls.py             -> É o arquivo de mapeamento entre rotas da aplicação e views
        * views são funcões ou classes que são chamadas quando uma rota é acessada pelo cliente
    manage.py             -> É o arquivo onde vamos chamar para passar os comandos do django (criar pacotes, aplicar migration, etc)

Para criar um novo pacote da aplicação, digitamos o comando:
    python manage.py startapp polls (polls é o nome da aplicação)

    Quando criamos um novo pacote dentro de django, ele cria uma pasta com a seguinte estrutura:
        - migrations/
        - admin.py
        - apps.my
        - models.py
        - tests.py
        - views.py

        - migrations/           -> DIretório que vai armazenar as migrations do pacote (alteraçao de tabelas, adição, etc)
        - admin.py              -> Serve pra configurarmos como as models serão exibidas no painel de admin
        - apps.py               -> Arquivo com as configurações do pacote. Geralmente apenas utilizado para registrar a aplicação
        - models.py             -> Módulo que serve para armazenar as models do pacote (os mapeamentos entre classes e tabelas do banco)
        - tests.py              -> Módulo onde escrevemos os testes unitários da aplicação
        - views.py              -> Módulo onde escrevemos as views (funções/classes chamdas quando uma rota é acessada)
        - urls.py               -> Módulo onde mapeamos (fazemos a associação) as rotas com as views que serão chamadas. Esse arquivo
        não é criado por padrão pelo Django.

Processo de retorno da requisição
    1. Acessamos a rota que foi configurada no Django
    2. O Django abre o arquivo urls.py do projeto
    3. Ele procura um padrão de texto que corresponda a URL que foi acessada
    4. Caso o Django encontre um padrão de texto que corresponda a URL que foi passada, ele executa a ação que foi configurada na rota
    5. No caso de include, o django vai abrir o arquivo de rotas do pacote que foi indicado (no nosso caso, polls.urls)
    6. Depois disso, o Django vai procurar um padrão de texto que corresponda a URL que foi colocado depois do padrão anterior (polls/)


Pesquisa
    - Questões
    - E cada Questão terá um conjunto de alternativas
    

Templates dentro do Django
    - Templates são arquivos html comuns que possuem marcações especiais. Essas marcações são definidas pela linguagem de templates do DJango. Basicamente, quando o template for carregado, essas marcações serão substituídas pelos valores que vamos passar para "dentro" dos templates.

    Tudo que está entre as marcações {% %} e {{ }} são comandos que serão executados
    e também variáveis que serão lidas para mostrar o seu valor na página.
    if...elif...else são marcações especiais dentro do template, que indicam um laço de condição

    {% if_latest_question_id %} verifica se a variável de template latest_question_list possui um valor. Se possuir, vai entrar no laço for abaixo
    Se não possuir, o template quando for renderizado (quando é carregado pela aplicação) vai exibir a mensagem "Não existem perguntas cadastradas"