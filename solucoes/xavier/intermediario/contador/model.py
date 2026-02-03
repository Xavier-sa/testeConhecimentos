def contar_palavras(texto):
    texto = texto.lower()
    palavras = texto.split()

    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return palavras, contador
