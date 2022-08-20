## Exercício

Vamos modelar a base de dados de um sistema simples de vendas.

`Lembrete: Gere as revisions sempre depois de criar a Model`

1) Criar a model UserProfile com os seguintes campos:
   * id (Integer, chave primária, e chave estrangeira para a model User)
   * first_name (String, não pode ser nulo)
   * last_name (String, não pode ser nulo)
   * birth_date  (DateTime, e pode ser nulo)
   * O nome da tabela no banco deve ser tb_users_profiles

2) Criar a model Product com os seguintes campos
   * id (Integer, chave primária, auto incremento)
   * name (String, nao pode ser nulo)
   * price (Float)
   * O nome da tabela no banco deve ser tb_products

3) Criar a model Order, com os seguites campos
   * id (Integer, chave primária, auto incremento)
   * user_id (Integer, chave estrangeira para a model User)
   * order_date (DateTime, não pode ser nulo)
   * description (String, pode ser nulo)
   * O nome da tabela no banco deve ser tb_orders

4) Criar a model OrderDetail, com os seguintes campos
   * product_id (Integer, chave primária, chave estrangeira para a model Product)
   * order_id (Integer, chave primária, chave estrangeira para a model Order)
   * quantity (Float, nao pode ser nulo)
   * description (String, pode ser nulo)
   * O nome da tabela no banco deve ser tb_orders_details