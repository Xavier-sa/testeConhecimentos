def pedir_texto():
    return input("Digite um texto: ")

def mostrar_resultado(total, contador):
    print("\nTotal de palavras:", total)
    print("\nContagem de palavras:")

    for palavra, quantidade in contador.items():
        print(f"{palavra}: {quantidade}")
