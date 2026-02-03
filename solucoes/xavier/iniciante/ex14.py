"""
Exercício 14 — Manipulação de string

Peça uma palavra ao usuário.
Mostre:
- Quantidade de letras
- A palavra em letras maiúsculas
"""

# Dica: len() e upper()

palavra = input("Informe uma palavra: ")

print("Quantidade de letras:", len(palavra))
print("Letras em maiúsculas:")

for letra in palavra:
    print(letra.upper())
