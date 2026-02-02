"""
Exercício 15 — Mini desafio

Peça um número ao usuário.
Se for positivo, imprima "Positivo".
Se for negativo, imprima "Negativo".
Se for zero, imprima "Zero".
"""

# Use if / elif / else


numero = int(input("Informe um  numero: "))

if numero > 0:
    print("Positivo")

elif numero < 0:
    print("Negativo")

elif numero == 0:
    print( "ZERO")

else:
    print("Entrada Invalida")