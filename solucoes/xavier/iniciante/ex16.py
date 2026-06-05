"""
Exercicio 16 - Controle de entrada em laboratorio de robotica

Um aluno podera entrar no laboratorio se:
- estiver matriculado
- possuir autorizacao do professor
- estiver usando os equipamentos de seguranca

Alunos monitores podem entrar sem autorizacao do professor.

Porem, ninguem podera entrar se estiver com ocorrencia disciplinar ativa.
"""

print("16. Controle de Entrada em Laboratorio de Robotica")

ocorrencia = input("O aluno possui ocorrencia disciplinar ativa? (s/n): ") == "s"

if ocorrencia:
    print("Resultado: Acesso Negado. Existe ocorrencia disciplinar ativa.")
else:
    matriculado = input("O aluno esta matriculado? (s/n): ") == "s"

    if not matriculado:
        print("Resultado: Acesso Negado. Aluno nao matriculado.")
    else:
        equipamentos = input("Esta usando os equipamentos de seguranca? (s/n): ") == "s"

        if not equipamentos:
            print("Resultado: Acesso Negado. Equipamentos de seguranca obrigatorios.")
        else:
            monitor = input("O aluno e monitor do laboratorio? (s/n): ") == "s"

            if monitor:
                print("Resultado: Acesso Permitido. Aluno monitor.")
            else:
                autorizacao = input("Possui autorizacao do professor? (s/n): ") == "s"

                if autorizacao:
                    print("Resultado: Acesso Permitido. Autorizacao confirmada.")
                else:
                    print("Resultado: Acesso Negado. Falta autorizacao do professor.")
