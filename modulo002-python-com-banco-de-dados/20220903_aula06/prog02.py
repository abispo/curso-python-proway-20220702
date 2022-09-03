import requests


def retorna_info_criptomoeda(criptomoeda):
    response = requests.get(f"https://api.coincap.io/v2/assets/{criptomoeda}")
    resultado = response.json()
    data = resultado.get("data")

    saida = {
        "nome": data.get("name"),
        "simbolo": data.get("symbol"),
        "preco": "{:.2f}".format(float(data.get("priceUsd"))),
        "volume24h": "{:.2f}".format(float(data.get("volumeUsd24Hr")))
    }

    return saida
