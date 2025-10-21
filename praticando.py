def coletar_dados(numero=12, entrada_func=input):
    dados = []

    nome = entrada_func("NOME:")
    idade = int(entrada_func("IDADE:"))
    profissao = entrada_func("PROFISSÃO:")
    salario = float(entrada_func("SALARIO:"))

    dados.append({
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "salario": salario
    })

    print(f"""
O player nº{numero} {'-'*20}

Nickname: {nome} {'-'*20}

Tem a idade de {idade} {'-'*20}

Sua Ocupação é {profissao} {'-'*20}

Possui um salario de {salario}
""")

def emprestimo(estado, valor, juros=0.02):
    print(f"Solicitando empréstimo de R${valor:.2f} com juros de {juros*100:.1f}%")
    estado['dividas'] += valor * (1 + juros)
    estado['patrimonio'] += valor
    estado['historico'].append(f"Empréstimo: +R${valor:.2f}, dívida aumentou para R${estado['dividas']:.2f}")
    print("Empréstimo concedido.")