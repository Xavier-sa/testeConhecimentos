
print(f"{'-'*12} Categorias:{'-'*13}")
infantil="5 - 7 anos"
iniciado="8 - 10 anos"
juvenil= "11 - 13 anos"
junior= "14 - 17 anos"
senior=" MAIORES DE 18 anos"
print(f"\tInfantil = {infantil}")
print(f"\tinciado = {iniciado}")
print(f"\tJuvenil = {juvenil}")
print(f"\tJunior = {junior}")
print(f"\tSenior = {senior}")
print(f"\t\t 0-Sair")
print(f"{'-'*37}")

#em desenvolimetno
while True:
    

    try:
        
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
        elif idadeAtleta== 0:
            print("Encerrando...!")
            break
        else:
            print("Idade Invalida")
            
            
    except ValueError:
            print("Erro: Entrada inválida! Por favor, digite um número inteiro.")

            
        #tratei erros e testado
