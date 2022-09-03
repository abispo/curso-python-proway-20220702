
def inverte_texto(texto):

    if isinstance(texto, str):
        return texto[::-1]

    raise Exception("Você deve passar um texto para a função")
