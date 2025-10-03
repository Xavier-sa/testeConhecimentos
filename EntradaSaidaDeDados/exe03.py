# 3. Escreva um programa para determinar a situação de uma aluno 
# (Aprovado/Exame/Reprovado) dada a sua assiduidade em percentagem e a nota 
# do teste (0 a 20), considerando a seguinte tabela.

# Assiduidade inferior a 75%                            Reprovado 
# Assiduidade entre 75% e 100% e nota até 5             Reprovado 
# Assiduidade entre 75% e 100% e nota de 5 até 9,5      Exame 
# Assiduidade entre 75% e 100% e nota entre 10 e 20     Aprovado

assiduidade = float(input("Digite a assiduidade do aluno (em %): "))
nota = float(input("Digite a nota do aluno (0 a 20): "))
if assiduidade < 75:
    situacao =  "Reprovado"
elif assiduidade >= 75 and assiduidade <= 100 and nota <= 5:
    situacao = "Reprovado"
elif assiduidade >= 75 and assiduidade <= 100 and nota > 5 and nota < 9.5:
    situacao = "Exame"
else:
    situacao = "Aprovado"
print(f"A situação do aluno é: {situacao}")