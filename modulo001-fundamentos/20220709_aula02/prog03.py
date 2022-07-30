"""
Tuplas
    - São estruturas de dados que podem também ser chamadas de
    containeres (estruturas que armazenam outros dados). Listas são:
    - Iteráveis
    - Indexáveis
    - Imutáveis
    - Tuplas são heterogêneas. Podem armazenar diversos tipos de
    dados, inclusive outras tuplas.
"""

if __name__ == "__main__":

    tpl = ("Banana", "Maçã",)

    # Tuplas são iteráveis
    for item in tpl:
        print(item)

    # Tuplas são indexáveis
    print(tpl[1])

    # Tuplas são imutáveis
    try:
        # Essa linha causará um TypeError
        tpl[1] = "Batata"
    except Exception:
        print("Você não pode fazer isso.")

    # Tuplas podem armazenar diversos tipos de itens, inclusive outras tuplas
    tpl2 = ("Nome", 23, [5, 6, 7], (2, 3,))
