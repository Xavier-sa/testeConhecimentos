"""
Exercício 07 — Par ou Ímpar

Peça um número ao usuário.
Informe se o número é par ou ímpar.
"""

# Dica: use o operador %

#resolucao maneira simples 
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


#Para eu usar futuramente em exercicios 
def verificar_paridade(numero: int) -> str:
    return "É PAR" if numero % 2 == 0 else "É ÍMPAR"


def executar():
    while True:
        try:
            numero = int(input("Informe o número (ou 0 para sair): "))

            if numero == 0:
                print("Programa encerrado.")
                break

            print(verificar_paridade(numero))

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


if __name__ == "__main__":
    executar()
