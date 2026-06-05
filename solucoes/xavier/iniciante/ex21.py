"""
Exercicio 21 - Aprovacao de compra interna

Uma compra podera ser aprovada se:
- o setor tiver orcamento
- o fornecedor estiver cadastrado
- a solicitacao estiver justificada

Diretores podem aprovar compras sem justificativa, desde que exista orcamento.

Nenhuma compra sera aprovada se o fornecedor estiver bloqueado.
"""

print("21. Aprovacao de Compra Interna")

fornecedor_bloqueado = input("O fornecedor esta bloqueado? (s/n): ") == "s"

if fornecedor_bloqueado:
    print("Resultado: Compra Negada. Fornecedor bloqueado.")
else:
    fornecedor_cadastrado = input("Fornecedor cadastrado? (s/n): ") == "s"

    if not fornecedor_cadastrado:
        print("Resultado: Compra Negada. Fornecedor nao cadastrado.")
    else:
        orcamento = input("O setor possui orcamento disponivel? (s/n): ") == "s"

        if not orcamento:
            print("Resultado: Compra Negada. Orcamento indisponivel.")
        else:
            diretor = input("O solicitante e diretor? (s/n): ") == "s"

            if diretor:
                print("Resultado: Compra Aprovada. Diretor com orcamento disponivel.")
            else:
                justificativa = input("A solicitacao possui justificativa? (s/n): ") == "s"

                if justificativa:
                    print("Resultado: Compra Aprovada.")
                else:
                    print("Resultado: Compra Negada. Falta justificativa.")
