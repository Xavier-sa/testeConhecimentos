#04. Escreva um programa que a partir da idade de uma pessoa expressa em anos, 
#meses e dias, apresente a idade apenas em dias (considerar o ano com 365 e cada 
# mês com 30 dias).

anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite os meses adicionais: "))
dias = int(input("Digite os dias adicionais: "))

anos_em_dias = anos * 365
meses_em_dias = meses * 30

idade_total_em_dias = anos_em_dias + meses_em_dias + dias

print(f"A idade em dias é {idade_total_em_dias}.")