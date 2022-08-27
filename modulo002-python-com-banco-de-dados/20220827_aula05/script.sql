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
    Utilizamos a Primeira Forma Normal para nos assegurarmos de que as tabelas possuem apenas
dados atômicos, ou seja, que os valores das colunas serão indivisíveis.
*/

USE curso_python_202207;

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
ON tu.id = tt.usuario_id
WHERE tu.id = 2;

/*
 * *******************************************************************************************************************************
 *
 * Segunda forma normal (2FN)
 * 
 * Utilizamos a segunda forma normal para garantir que um quaisquer campos da tabela sejam dependentes de todas as partes da chave
 * primária. Uma tabela está na 2FN quando:
 * Ela está na 1FN
 * E todas as colunas dessa tabela dependem de todas as partes da chave primária
 */

CREATE TABLE tb_produtos(
	id INTEGER AUTO_INCREMENT,
	nome_produto VARCHAR(100) NOT NULL,
	preco_unitario FLOAT NOT NULL,
	description TEXT NULL,
	PRIMARY KEY(id)
);


/*
 * Como a coluna nome_produto depende apenas de uma parte da chave primária (coluna produto_id), para aplicar a 2FN precisamos excluir essa
 * coluna da tabela
 */
CREATE TABLE tb_pedidos(
	id INTEGER AUTO_INCREMENT,
	produto_id INTEGER NOT NULL,
	nome_produto VARCHAR(100) NOT NULL,
	observacoes TEXT NOT NULL,
	PRIMARY KEY(id, produto_id),
	FOREIGN KEY (produto_id) REFERENCES tb_produtos(id)
);

ALTER TABLE tb_pedidos DROP COLUMN nome_produto;

/*
 * Terceira Forma Normal (3FN)
 * 
 * Utizamos a Terceira Forma Normal para garantir que não existam colunas não chave de uma tabela que dependam de outras colunas não
 * chave da mesma tabela. Uma tabela está na 3FN quando:
 * Está na 2FN
 * Não existem atributos não-chave dependentes de outros atributos não-chave
 */

CREATE TABLE IF NOT EXISTS tb_estoque(
	id INTEGER AUTO_INCREMENT,
	produto_id INTEGER NOT NULL,
	preco_unitario FLOAT NOT NULL,
	quantidade INTEGER NOT NULL,
	multiplicador FLOAT NOT NULL,
	preco_final FLOAT NOT NULL		# A coluna preco_final depende dos valores de 2 colunas não-chave (preco_unitario e multiplicador). Nesse caso devemos excluir essa coluna
	PRIMARY KEY(id, produto_id),
	FOREIGN KEY(produto_id) REFERENCES tb_produtos(id)
);

ALTER TABLE tb_estoque DROP COLUMN preco_final

INSERT INTO tb_produtos(nome_produto, preco_unitario) VALUES ("Sabonete", 1);
INSERT INTO tb_produtos(nome_produto, preco_unitario) VALUES ("Shampoo", 5);
INSERT INTO tb_produtos(nome_produto, preco_unitario) VALUES ("Toalha", 20);

SELECT * FROM tb_produtos tp ;

INSERT INTO tb_estoque(produto_id, preco_unitario, quantidade, multiplicador) VALUES(
	1, 1, 100, 1.6
);
INSERT INTO tb_estoque(produto_id, preco_unitario, quantidade, multiplicador) VALUES (
	2, 5, 50, 2
);

INSERT INTO tb_estoque(produto_id, preco_unitario, quantidade, multiplicador) VALUES (
	3, 20, 20, 1.3
);

SELECT produto_id, quantidade, preco_unitario * multiplicador AS preco_final FROM tb_estoque te ;

