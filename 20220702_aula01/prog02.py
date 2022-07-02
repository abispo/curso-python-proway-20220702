"""
Operadores matemáticos
+ (soma)
- (subtração)
/ (divisão)
* (multiplicação)
% (módulo (resto da divisão))
** (exponenciação)

Operadores de Comparação
> (Maior que)
>= (Maior ou igual a)
< (Menor que)
=< (Menor ou igual a)
== (Igual a)
!= (Diferente de)

Operadores lógicos
or (Ou)
and (E)
not (Não)   (operador unário)

Estruturas de decisão (if... elif... else)

if True -> executa o bloco de código

"""

if __name__ == '__main__':

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    # Devido a precedência de operadores, precisamos informar ao interpretador
    # que a soma das 3 notas deve ser feita primeiro, antes da divisão por 3
    media = (nota1 + nota2 + nota3) / 3

    # Formatando a saída para ser mostrada apenas 1 casa depois da vírgula
    print(f"A média final do aluno é de {media:.1f}")

    """
    Se a média do aluno for menor que 5, mostrar a mensagem "Aluno reprovado"
    Se a média for maior ou igual a 5 E menor que 7, mostrar a mensagem
    "Aluno em recuperação"
    Se a média for maior ou igual
     que 7, mostrar a mensagem "Aluno aprovado"
    
    if... elif... else
    
    if/elif condicao for verdadeira:
        bloco de codigo
    
    """

    if media < 5:
        print("O aluno foi reprovado")

    elif media >= 5 and media < 7:
        print("O aluno está de recuperação")

    else:
        print("O aluno foi aprovado")
