"""
Trabalhando com arquivos texto em Python (Leitura/Escrita)

Também chamado de Entrada/Saída em arquivos (Input/Output | I/O)

Quando utilizamos as funções built-in input() e print(), estamos trabalhando com Entrada e Saída via terminal
Para trabalharmos com arquivos, utilizamos a função built-in open()

Modos de abertura de arquivo

'r'     -> Somente leitura (padrão)
'w'     -> Abre para escrita, truncando o arquivo se ele existir, cria se não existir
'x'     -> Apenas cria o arquivo, se ele já existir, gera um erro
'a'     -> Abre para escrita, porém ele adicionado o novo conteúdo no final do arquivo

'b'     -> Abre o arquivo no modo binário
't'     -> Abre o arquivo no modo texto (padrão)

'+'     -> Abre o arquivo para atualização ('r+')
"""

if __name__ == "__main__":
    """
    Utilizando open() para abrir um arquivo.
    Precisamos passar o nome do arquivo (argumento obrigatório)
    Se não especificarmos o modo de abertura, por padrão esse arquivo será aberto no modo somente-leitura.
    
    """

    # Se esse arquivo não existir, será gerado um erro FileNotFoundError
    # O argumento mode="w" indica que vamos abrir esse arquivo para escrita
    _file = open("prog01.txt", mode="w", encoding="utf-8")

    """
    Quando abrimos um arquivo no modo de escrita ("w"), se o arquivo especificado não existir, ele é criado.
    Se o arquivo já existir, o seu conteúdo é truncado (sobrescrito)
    """

    # Escrevendo uma linha no arquivo utilizando o método write()
    _file.write("Curso de Python 2022\n\n")

    # Utilizamos o comando especial '\n' para quebra de linha

    linhas = [
        "Fundamentos\n", "Banco de dados\n", "Programação WEB\n"
    ]

    # Podemos escrever várias linhas de uma vez utilizando o método writelines()
    _file.writelines(linhas)

    # Sempre que abrirmos um arquivo, devemos fechá-lo
    _file.close()

    # Vamos abrir o arquivo no modo 'a' (append) utilizando a palavra reservada with (gerenciador de contexto)
    # Nesse modo, o arquivo não é sobrescrito, mas sim o novo conteúdo é adicionado ao final do arquivo.
    with open("prog01.txt", mode='a', encoding="utf-8") as _file:
        _file.write("\nEsse curso foi iniciado em 02/07/2022.")

        # Quando abrimos o arquivo dessa maneira, não precisamos fechá-lo com close(), pois ele é
        # automaticamente fechado

    # Abrindo o arquivo
    # Se não for passado, o modo de abertura é definido como 'r' leitura
    with open("prog01.txt", mode="r", encoding="utf-8") as _file:

        # O método tell() mostra a posição atual do cursor dentro do arquivo
        print(_file.tell())

        # O método read() retorna o conteúdo completo do arquivo se o limite não for passado. O valor retornado
        # é uma string
        conteudo = _file.read()
        print(conteudo)

        # O cursor do arquivo estará no último byte (posição) devido ao uso do método read()
        print(_file.tell())

        # O método seek() serve para reposicionar o cursor em qualquer lugar do arquivo
        _file.seek(0)

        # O método readline() retorna uma linha inteira do arquivo, até o limite especificado
        conteudo = _file.readline()
        print(conteudo)

        # O método readlines() lê o conteúdo restante do arquivo
        conteudo = _file.readlines()
        print(conteudo)


    # Lendo o conteúdo do arquivo de maneira sequencial
    with open("prog01.txt", mode="r", encoding="utf-8") as _file:

        for linha in _file:
            print(linha)