# 2. Escreva um programa que ajude um comerciante a calcular o valor de venda a 
# partir de um valor de compra de um dado produto.

# Valor da Compra         Valor da Venda 
# Valor < 10,00           70% de lucro 
# 10,00 ≤ Valor < 30,00   50% de lucro 
# 30,00 ≤ Valor < 50,00   40% de lucro 
# Valor ≥ 50,00           30% de lucro

valor_compra = float(input("Digite o valor de compra do produto: R$ ")) 

if valor_compra < 10:
    valor_venda = valor_compra * 1.7
elif valor_compra >= 10 and valor_compra < 30:
    valor_venda = valor_compra * 1.5
elif valor_compra >= 30 and valor_compra < 50:
    valor_venda = valor_compra * 1.4
else:
    valor_venda = valor_compra * 1.3

print(f"O valor de venda do produto é R$ {valor_venda:.2f}")