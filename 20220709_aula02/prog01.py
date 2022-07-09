from random import randint

if __name__ == '__main__':
    for item in ["Bolsa", "Sapato", "Relógio"]:
        print(item)

    numero = 0

    while numero < 10:
        numero = randint(1, 15)
        print(numero)
