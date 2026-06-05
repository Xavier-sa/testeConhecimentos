"""
Exercicio 24 - Solicitacao de estagio interno

Um aluno podera iniciar estagio interno se:
- possuir matricula ativa
- possuir media minima 7
- possuir frequencia minima 75%

Alunos indicados por coordenador podem iniciar com media 6.

Nenhum aluno podera iniciar se possuir pendencia documental.
"""

print("24. Solicitacao de Estagio Interno")

pendencia_documental = input("Possui pendencia documental? (s/n): ") == "s"

if pendencia_documental:
    print("Resultado: Estagio Negado. Pendencia documental.")
else:
    matricula_ativa = input("Matricula ativa? (s/n): ") == "s"

    if not matricula_ativa:
        print("Resultado: Estagio Negado. Matricula inativa.")
    else:
        frequencia = float(input("Informe a frequencia (%): "))

        if frequencia < 75:
            print("Resultado: Estagio Negado. Frequencia insuficiente.")
        else:
            media = float(input("Informe a media do aluno: "))
            indicado = input("Foi indicado por coordenador? (s/n): ") == "s"

            if media >= 7 or (indicado and media >= 6):
                print("Resultado: Estagio Aprovado.")
            else:
                print("Resultado: Estagio Negado. Media insuficiente.")
