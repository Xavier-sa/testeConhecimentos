eleitores_municipio= int(input("Informe o numero Total de eleitores:\n"))
print(f"{eleitores_municipio:.2f}")

voto_branco = int(input("Votos BRANCO:"))
voto_nulo = int(input("Votos NULO:"))
voto_valido= int(input("Votos VALIDO:"))


total_votos= voto_branco + voto_nulo + voto_valido
print(f"O total de Votos do Municipio é {total_votos}")
porcentos_branco = voto_branco/eleitores_municipio * 100
print(f"{porcentos_branco:.2f}%")
porcentos_nulo = voto_nulo/eleitores_municipio * 100
print(f"{porcentos_nulo:.2f}%")
porcentos_valido = voto_valido/eleitores_municipio * 100
print(f"{porcentos_valido:.2f}%")

#notei erro faltou declarar uma variavel para a falta/abstencao

nao_voto = eleitores_municipio -voto_branco - voto_nulo -voto_valido
nao_votou = nao_voto/eleitores_municipio * 100
print(f"Não votaram aproximadmente {nao_votou:.2f}%")
#preciso fazer a porcentagem de cada tipo de voto com os eleitores






