# 1. Escreva um programa que receba a idade de um atleta e determine a sua 
# categoria segundo a tabela apresentada:

# Categoria     Idade 
# Infantil      5 - 7 anos 
# Iniciado      8 - 10 anos 
# Juvenil       11 - 13 anos 
# Junior        14 - 17 anos 
# Sénior        Maiores de 18 anos

idade = int(input("Digite a idade do atleta: "))

if idade >= 5 and idade <= 7:
    print("Infantil")
elif idade >= 8 and idade <= 10:
    print("Iniciado")
elif idade >= 11 and idade <= 13:
    print("Juvenil")
elif idade >= 14 and idade <= 17:
    print("Junior")
else:
    print("Sênior")