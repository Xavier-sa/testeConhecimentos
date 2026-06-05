"""
Exercicio 19 - Liberacao de equipamento de TI

Um colaborador podera retirar notebook se:
- possuir cadastro ativo
- possuir termo assinado
- nao tiver equipamento pendente de devolucao

Coordenadores podem retirar sem termo assinado, mas devem ter cadastro ativo.

Nenhum equipamento sera liberado se o colaborador estiver bloqueado.
"""

print("19. Liberacao de Equipamento de TI")

bloqueado = input("O colaborador esta bloqueado? (s/n): ") == "s"

if bloqueado:
    print("Resultado: Liberacao Negada. Colaborador bloqueado.")
else:
    cadastro_ativo = input("Cadastro ativo? (s/n): ") == "s"

    if not cadastro_ativo:
        print("Resultado: Liberacao Negada. Cadastro inativo.")
    else:
        pendente = input("Possui equipamento pendente de devolucao? (s/n): ") == "s"

        if pendente:
            print("Resultado: Liberacao Negada. Existe equipamento pendente.")
        else:
            coordenador = input("E coordenador? (s/n): ") == "s"

            if coordenador:
                print("Resultado: Notebook liberado. Coordenador autorizado.")
            else:
                termo = input("Assinou o termo de responsabilidade? (s/n): ") == "s"

                if termo:
                    print("Resultado: Notebook liberado.")
                else:
                    print("Resultado: Liberacao Negada. Termo nao assinado.")
