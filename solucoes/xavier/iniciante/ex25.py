"""
Exercicio 25 - Autorizacao de desconto especial

Um cliente podera receber desconto se:
- for cadastrado
- estiver com pagamento em dia
- tiver comprado acima de R$ 500

Clientes VIP podem receber desconto com compras acima de R$ 300.

Nenhum desconto sera concedido se o cliente possuir bloqueio comercial.
"""

print("25. Autorizacao de Desconto Especial")

bloqueio = input("Cliente possui bloqueio comercial? (s/n): ") == "s"

if bloqueio:
    print("Resultado: Desconto Negado. Cliente com bloqueio comercial.")
else:
    cadastrado = input("Cliente cadastrado? (s/n): ") == "s"

    if not cadastrado:
        print("Resultado: Desconto Negado. Cliente nao cadastrado.")
    else:
        pagamento_dia = input("Pagamento esta em dia? (s/n): ") == "s"

        if not pagamento_dia:
            print("Resultado: Desconto Negado. Pagamento em atraso.")
        else:
            valor_compra = float(input("Informe o valor da compra: R$ "))
            vip = input("Cliente e VIP? (s/n): ") == "s"

            if valor_compra > 500 or (vip and valor_compra > 300):
                print("Resultado: Desconto Aprovado.")
            else:
                print("Resultado: Desconto Negado. Valor minimo nao atingido.")
