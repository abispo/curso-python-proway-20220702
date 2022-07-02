
"""
Devemos mostrar o salário do funcionário de acordo com o tipo de funcionário
que está sendo processado. Temos 3 tipos de funcionários:
    - Funcionário CLT -> Valor do salário fixo
    - Funcionário Terceirizado -> O salário é calculado pela multiplicação
    da quantidade de horas trabalhadas vezes o valor da hora
    - Funcionário comissionado: O salário é calculado pela porcentagem do valor
    total das vendas que ele realizou. Exemplo:
        João vendeu 10000 reais no mês
        A comissão dele é de 20%
        O salário de João é de 2000 reais
    No nosso exercício, a porcentagem do valor recebido pelo funcionário
    comissionado é livre.

    Python é uma linguagem case-sensitive
    "clt" é diferente de "CLT"
    salario é diferente de Salario

"""

if __name__ == "__main__":

    print("== CÁLCULO DE SALÁRIO ==")

    tipo_funcionario = input("Informe o tipo de funcionário (CLT, TERCEIRIZADO, COMISSIONADO): ").upper()
    salario = 0

    if tipo_funcionario == "CLT":
        salario = float(input("Informe o salário: "))

    elif tipo_funcionario == "TERCEIRIZADO":
        quantidade_horas = int(input("Informe a quantidade de horas trabalhadas: "))
        valor_hora = float(input("Informe o valor da hora trabalhada: "))

        salario = quantidade_horas * valor_hora

    elif tipo_funcionario == "COMISSIONADO":
        valor = float(input("Informe o valor de vendas do funcionário no período: "))
        porcentagem = float(input("Informe o valor da porcentagem de comissão: "))

        salario = valor * (porcentagem / 100)

    else:
        print(f"O tipo de funcionário {tipo_funcionario} não existe")

    if salario > 0:
        print(f"O salário do funcionário é de {salario:.2f}")