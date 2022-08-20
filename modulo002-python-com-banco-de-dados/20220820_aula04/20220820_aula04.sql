/*
Normaliza��o de tabelas

Normaliza��o de tabelas pode ser definida como um conjunto de passos ou verifica��es que s�o
realizados no momento onde estamos desenhando a arquitetura de armazenamento dos dados de um
sistema qualquer. Utilizamos a normaliza��o de dados para:
    * Evitar redund�ncia de dados (colunas que se repetem ou que n�o s�o necess�rios)
    * Assegurar que o modelo condiz com a realidade que est� sendo modelada

Para atingir esse objetivo, aplicamos as formas normais na fase de desenho do banco de dados.
Vamos trat�-las como Primeira Forma Normal(1FN), Segunda Forma Normal(2FN) e Terceira Forma
Normal(3FN).

1FN
    Utilizamos a Primeira Forma Normal para nos assegurmos de que as tabelas possuem apenas
dados at�micos, ou seja, que os valores das colunas ser�o indivis�veis.

*/

USE aula_04;

CREATE TABLE tb_usuarios(
	id INTEGER AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	telefones TEXT NOT NULL,
	PRIMARY KEY(id)
);

/*
 * Aqui percebemos que a coluna telefones da tb_usuarios possui mais de 1 valor para telefone. Ou seja, essa coluna
 * armazena valores que n�o s�o at�micos
 */
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Maria", "5511976389002");
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Bruna", "5511987683211, 5547988877143");
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Carla", "5547981333227");

SELECT * FROM tb_usuarios tu ;

/*
 * Para resolver isso, vamos criar a tabela tb_telefones que ir� armazenar os telefones de todos os usu�rios que est�o
 * na tabela tb_usuarios. E para relacionar um usu�rio com o(s) seus telefones, ser� criada uma chave estrangeira na
 * tb_telefones, que far� refer�ncia a tabela tb_usuarios
 */

CREATE TABLE tb_telefones(
	id INTEGER AUTO_INCREMENT,
	usuario_id INTEGER NOT NULL,
	telefone VARCHAR(20),
	PRIMARY KEY(id),
	FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);

/*
 * Dessa maneira, a coluna telefone ser� indivis�vel, pois ter� apenas 1 valor para telefone
 */

INSERT INTO tb_telefones (usuario_id, telefone) VALUES (1, "5511976389002");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (2, "5511987683211");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (2, "5547988877143");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (3, "5547981333227");

SELECT * FROM tb_telefones tt ;

/*
 * Como agora n�o precisamos mais da informa��o de telefone na tb_usuarios, podemos excluir essa coluna da tabela
 */

ALTER TABLE tb_usuarios DROP COLUMN telefones;

/*
 * Cl�usula JOIN que mostrar� os usu�rios e seus respectivos telefones
 */

SELECT tu.id, tu.nome, tt.telefone FROM tb_usuarios tu
INNER JOIN tb_telefones tt 
ON tu.id = tt.usuario_id ;