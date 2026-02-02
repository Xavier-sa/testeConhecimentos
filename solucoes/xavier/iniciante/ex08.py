"""
Exercício 08 — Função simples

Crie uma função chamada saudacao.
Ela deve receber um nome e imprimir:

"Olá, <nome>!"
"""

# Crie a função abaixo
def saudacao(nome: str) -> None:
    print(f"Olá, {nome}!")


nome = input("Informe o nome: ")
saudacao(nome)
