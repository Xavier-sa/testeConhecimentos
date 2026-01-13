"""
Exercício 03 — Condição

Peça ao usuário uma idade.
Se for maior ou igual a 18, mostre:
"Acesso permitido"

Caso contrário:
"Acesso negado"
"""

idade = int(input("Qual sua idade?"))

if not idade > 17:
    print("Acesso Negado")

else:
    print("Acesso Permitido")
    
