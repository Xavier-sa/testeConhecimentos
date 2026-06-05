"""
Exercicio 18 - Autorizacao de viagem corporativa

Um funcionario podera viajar se:
- possuir cadastro ativo
- possuir solicitacao aprovada
- existir orcamento disponivel

Gerentes podem viajar sem aprovacao previa, desde que exista orcamento.

Ninguem podera viajar se estiver com prestacao de contas pendente.
"""

print("18. Autorizacao de Viagem Corporativa")

prestacao_pendente = input("Existe prestacao de contas pendente? (s/n): ") == "s"

if prestacao_pendente:
    print("Resultado: Viagem Negada. Prestacao de contas pendente.")
else:
    cadastro_ativo = input("O funcionario possui cadastro ativo? (s/n): ") == "s"

    if not cadastro_ativo:
        print("Resultado: Viagem Negada. Cadastro inativo.")
    else:
        orcamento = input("Existe orcamento disponivel? (s/n): ") == "s"

        if not orcamento:
            print("Resultado: Viagem Negada. Orcamento indisponivel.")
        else:
            gerente = input("O funcionario e gerente? (s/n): ") == "s"

            if gerente:
                print("Resultado: Viagem Aprovada. Gerente com orcamento disponivel.")
            else:
                aprovada = input("A solicitacao foi aprovada? (s/n): ") == "s"

                if aprovada:
                    print("Resultado: Viagem Aprovada.")
                else:
                    print("Resultado: Viagem Negada. Solicitacao sem aprovacao.")
