"""
Exercicio 20 - Inscricao em campeonato escolar

Um aluno podera participar se:
- estiver matriculado
- possuir frequencia minima de 80%
- possuir autorizacao dos responsaveis

Alunos maiores de idade nao precisam de autorizacao.

Ninguem podera participar se estiver suspenso pela coordenacao.
"""

print("20. Inscricao em Campeonato Escolar")

suspenso = input("O aluno esta suspenso pela coordenacao? (s/n): ") == "s"

if suspenso:
    print("Resultado: Inscricao Negada. Aluno suspenso.")
else:
    matriculado = input("O aluno esta matriculado? (s/n): ") == "s"

    if not matriculado:
        print("Resultado: Inscricao Negada. Aluno nao matriculado.")
    else:
        frequencia = float(input("Informe a frequencia do aluno (%): "))

        if frequencia < 80:
            print("Resultado: Inscricao Negada. Frequencia insuficiente.")
        else:
            idade = int(input("Informe a idade do aluno: "))

            if idade >= 18:
                print("Resultado: Inscricao Aprovada. Aluno maior de idade.")
            else:
                autorizacao = input("Possui autorizacao dos responsaveis? (s/n): ") == "s"

                if autorizacao:
                    print("Resultado: Inscricao Aprovada.")
                else:
                    print("Resultado: Inscricao Negada. Falta autorizacao dos responsaveis.")
