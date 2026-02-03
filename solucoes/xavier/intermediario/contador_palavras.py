texto = input("Digite um texto: ")

texto = texto.lower()

palavras = texto.split()

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("\nTotal de palavras:", len(palavras))

print("\nContagem de palavras:")
for palavra, quantidade in contador.items():
    print(f"{palavra}: {quantidade}")
