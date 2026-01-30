"""
Exercício 07 — Par ou Ímpar

Peça um número ao usuário.
Informe se o número é par ou ímpar.
"""

# Dica: use o operador %


while True:
    stringNumero = "Informe o número (ou 0 para sair): "
    numero = int(input(stringNumero))

    if numero == 0:
        print("Programa encerrado.")
        break

    if numero % 2 == 0:
        print("É PAR")
    else:
        print("É ÍMPAR")
