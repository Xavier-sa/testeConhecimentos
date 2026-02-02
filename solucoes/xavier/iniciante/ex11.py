"""
Exercício 11 — Contador

Peça um número ao usuário.
Conte de 1 até esse número e imprima.
"""

# Exemplo:
# Entrada: 5
# Saída: 1 2 3 4 5


numero = int(input("Informe o numero da cotagem regressiva:"))

contador = 0
for i in range (1,numero):
    print(i)
    
