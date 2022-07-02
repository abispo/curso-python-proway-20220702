# Crie um script que receba 2 números, faça a soma desses 2 números
# e imprima o valor da soma desses números
# > Informe o primeiro número: 10
# > Informe o segundo número: 15
# > O resultado da soma de 10 e 15 é 25

if __name__ == "__main__":

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    resultado = numero1 + numero2

    print(f"O resultado da soma de {numero1} e {numero2} é {resultado}")
