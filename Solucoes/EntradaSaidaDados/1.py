
print(f"{'-'*10} Categorias:{'-'*10}")
infantil="5 - 7 anos"
iniciado="8 - 10 anos"
juvenil= "11 - 13 anos"
junior= "14 - 17 anos"
senior=" MAIORES DE 18 anos"
print(f"Infantil = {infantil}")
print(f"inciado = {iniciado}")
print(f"Juvenil = {juvenil}")
print(f"Junior = {junior}")
print(f"Senior = {senior}")
#em desenvolimetno
idadeAtleta = int(input("Qual a idade do atleta?:"))
if idadeAtleta >=18:
    print(senior)
elif 5 <= idadeAtleta <=7:
    print(infantil)
elif 8 <= idadeAtleta <=10:
    print(iniciado)
elif 11<= idadeAtleta <=13:
    print(juvenil)
elif 14 <= idadeAtleta <=17:
    print(junior)
else:
    print("Idade Invalida")
