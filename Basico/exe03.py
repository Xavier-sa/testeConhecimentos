# 3. Escreva um programa para ler o número total de eleitores de um município, o 
# numero de votos brancos, nulos e válidos. Apresente a percentagem que cada 
# um representa em relação ao total de eleitores.

total_eleitores = int(input("Digite o número total de eleitores do município: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

total_votos = votos_brancos + votos_nulos + votos_validos
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

print(f"O total de votos é {total_votos}.")
print(f"O percentual de votos brancos é {percentual_brancos:.2f}%.")
print(f"O percentual de votos nulos é {percentual_nulos:.2f}%.")
print(f"O percentual de votos válidos é {percentual_validos:.2f}%.")