from model import contar_palavras
import view

def executar():
    texto = view.pedir_texto()

    palavras, contador = contar_palavras(texto)

    view.mostrar_resultado(len(palavras), contador)
