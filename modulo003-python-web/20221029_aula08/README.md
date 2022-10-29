
# PROJETO -> Finanças Pessoais

* Sistema web onde podemos registrar entradas e saídas, como se fosse uma conta bancária.
* O sistema será baseado em contas financeiras

Conta (Conta Corrente Viacredi)
0

Conta Salario Proway
-1000

Conta Viacredi
1000

Transação   -> Uma transferência entre contas
Conta de débito -> Conta salário Proway
Conta de crédito -> Conta corrente Viacredi
Valor da transação: 1000

Conta de água Samae

Transação
Conta de débito -> Conta Viacredi
Conta de crédito    -> Conta samae
Valor de transação  150

Conta viacredi -> 850
Conta Samae     -> 150
---------------------------------------------------------

Model FinancialAccount
* id
* user_id       ( chave estrangeira para a model user )
* name          ( nome da conta )
* balance       ( saldo )
* created_at    ( data de criação )


Model Transaction
* id
* debit_account     ( chave estrangeira para a conta que foi debitada )     related_name="debit_account"
* credit_account    ( chave estrangeira para a conta que foi creditada )    related_name="credit_account"
* value             ( valor da transação )
* timestamp         ( data e hora da transação )

Quando o usuário entrar, serão exibidos 2 links
    - Link com a lista de contas
        - Cada item da lista será um link para o detalhe da conta
        - Na página de detalhe da conta, deve ser exibidas as seguintes informações:
            - Saldo atual da conta
            - As transações realizadas nessa conta
            - Cada transação será um link para o detalhe da transação

    - Link com a lista de transações
        - A lista deve ter paginação de 10 registros por página
        - Cada item da lista deve ser um link para o detalhe da transação
        - Dentro do detalhe da transação, cada conta também será um link para o detalhe da conta

Detalhes
    - Todo usuário deve estar logado para visualizar as informações do sistema
    - Cada usuário deve ter acesso apenas as informações sobre suas contas e transações. Não pode ser possível um
    usuário acessar as informações de transação e de contas de outros usuários
    - Não é permitido um usuário fazer uma transação em nome de outro usuário

tr = Transaction.objects.first()
tr.debit_account.user_id