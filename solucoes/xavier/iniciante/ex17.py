"""
Exercicio 17 - Solicitacao de bolsa de estudos

Um aluno podera receber bolsa se:
- possuir media maior ou igual a 8
- possuir frequencia minima de 85%
- possuir renda familiar menor que R$ 3.000

Alunos com destaque em olimpiadas podem concorrer com media minima 7.

Nenhum aluno podera receber bolsa se possuir advertencia grave.
"""

print("17. Solicitacao de Bolsa de Estudos")

advertencia_grave = input("O aluno possui advertencia grave? (s/n): ") == "s"

if advertencia_grave:
    print("Resultado: Bolsa Negada. Advertencia grave registrada.")
else:
    renda = float(input("Informe a renda familiar: R$ "))
    frequencia = float(input("Informe a frequencia do aluno (%): "))

    if renda >= 3000:
        print("Resultado: Bolsa Negada. Renda familiar acima do limite.")
    elif frequencia < 85:
        print("Resultado: Bolsa Negada. Frequencia insuficiente.")
    else:
        media = float(input("Informe a media do aluno: "))
        destaque = input("Possui destaque em olimpiadas academicas? (s/n): ") == "s"

        if media >= 8 or (destaque and media >= 7):
            print("Resultado: Bolsa Aprovada.")
        else:
            print("Resultado: Bolsa Negada. Media insuficiente.")
