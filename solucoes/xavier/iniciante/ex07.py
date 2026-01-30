"""
Exercício 07 — Par ou Ímpar

Peça um número ao usuário.
Informe se o número é par ou ímpar.
"""

# Dica: use o operador %


stringNumero = "Informe o numero:"
numero = int(input(stringNumero))

if numero % 2 == 0:
    print("É PAR")
else:
    print("É ÍMPAR")
