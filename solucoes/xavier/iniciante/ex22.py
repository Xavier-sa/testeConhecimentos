"""
Exercicio 22 - Atendimento prioritario em clinica

Um paciente podera ser atendido se:
- possuir cadastro
- possuir horario agendado
- possuir documentos validos

Casos de emergencia podem ser atendidos sem horario agendado.

Nenhum atendimento sera realizado se o cadastro estiver bloqueado.
"""

print("22. Atendimento Prioritario em Clinica")

cadastro_bloqueado = input("O cadastro do paciente esta bloqueado? (s/n): ") == "s"

if cadastro_bloqueado:
    print("Resultado: Atendimento Negado. Cadastro bloqueado.")
else:
    cadastro = input("Paciente possui cadastro? (s/n): ") == "s"

    if not cadastro:
        print("Resultado: Atendimento Negado. Paciente sem cadastro.")
    else:
        documentos = input("Documentos estao validos? (s/n): ") == "s"

        if not documentos:
            print("Resultado: Atendimento Negado. Documentos invalidos.")
        else:
            emergencia = input("E caso de emergencia? (s/n): ") == "s"

            if emergencia:
                print("Resultado: Atendimento Aprovado. Caso de emergencia.")
            else:
                agendado = input("Possui horario agendado? (s/n): ") == "s"

                if agendado:
                    print("Resultado: Atendimento Aprovado.")
                else:
                    print("Resultado: Atendimento Negado. Nao ha horario agendado.")
