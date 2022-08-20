/*
Normalização de tabelas

Normalização de tabelas pode ser definida como um conjunto de passos ou verificações que são
realizados no momento onde estamos desenhando a arquitetura de armazenamento dos dados de um
sistema qualquer. Utilizamos a normalização de dados para:
    * Evitar redundância de dados (colunas que se repetem ou que não são necessários)
    * Assegurar que o modelo condiz com a realidade que está sendo modelada

Para atingir esse objetivo, aplicamos as formas normais na fase de desenho do banco de dados.
Vamos tratá-las como Primeira Forma Normal(1FN), Segunda Forma Normal(2FN) e Terceira Forma
Normal(3FN).

1FN
    Utilizamos a Primeira Forma Normal para nos assegurmos de que as tabelas possuem apenas
dados atômicos, ou seja, que os valores das colunas serão indivisíveis.

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
 * armazena valores que não são atômicos
 */
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Maria", "5511976389002");
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Bruna", "5511987683211, 5547988877143");
INSERT INTO tb_usuarios(nome, telefones) VALUES ("Carla", "5547981333227");

SELECT * FROM tb_usuarios tu ;

/*
 * Para resolver isso, vamos criar a tabela tb_telefones que irá armazenar os telefones de todos os usuários que estão
 * na tabela tb_usuarios. E para relacionar um usuário com o(s) seus telefones, será criada uma chave estrangeira na
 * tb_telefones, que fará referência a tabela tb_usuarios
 */

CREATE TABLE tb_telefones(
	id INTEGER AUTO_INCREMENT,
	usuario_id INTEGER NOT NULL,
	telefone VARCHAR(20),
	PRIMARY KEY(id),
	FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);

/*
 * Dessa maneira, a coluna telefone será indivisível, pois terá apenas 1 valor para telefone
 */

INSERT INTO tb_telefones (usuario_id, telefone) VALUES (1, "5511976389002");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (2, "5511987683211");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (2, "5547988877143");
INSERT INTO tb_telefones (usuario_id, telefone) VALUES (3, "5547981333227");

SELECT * FROM tb_telefones tt ;

/*
 * Como agora não precisamos mais da informação de telefone na tb_usuarios, podemos excluir essa coluna da tabela
 */

ALTER TABLE tb_usuarios DROP COLUMN telefones;

/*
 * Cláusula JOIN que mostrará os usuários e seus respectivos telefones
 */

SELECT tu.id, tu.nome, tt.telefone FROM tb_usuarios tu
INNER JOIN tb_telefones tt 
ON tu.id = tt.usuario_id ;