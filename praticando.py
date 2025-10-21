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
    
    
    
def financiamento(estado, valor, juros=0.015):
    print(f"Financiando bem no valor de R${valor:.2f} com juros de {juros*100:.1f}%")
    estado['dividas'] += valor * (1 + juros)
    estado['patrimonio'] += valor
    estado['historico'].append(f"Financiamento: +R${valor:.2f}, dívida aumentou para R${estado['dividas']:.2f}")
    print("Financiamento aprovado.")
    
    
def alienacao(estado, valor):
    print(f"Alienando bem no valor de R${valor:.2f}")
    if valor > estado['patrimonio']:
        print("Não é possível alienar valor maior que o patrimônio atual.")
        return
    estado['patrimonio'] -= valor
    # Usar o dinheiro para pagar dívidas, se houver
    if estado['dividas'] > 0:
        pago = min(valor, estado['dividas'])
        estado['dividas'] -= pago
        estado['historico'].append(f"Alienação: vendeu R${valor:.2f}, pagou dívidas R${pago:.2f}")
        print(f"Dívidas reduzidas em R${pago:.2f}")
    else:
        estado['historico'].append(f"Alienação: vendeu R${valor:.2f}, sem dívidas para pagar")
    print("Alienação realizada.")
    
def elevacao_patrimonio(estado, valor):
    print(f"Aumentando patrimônio em R${valor:.2f}")
    estado['patrimonio'] += valor
    estado['historico'].append(f"Aumento patrimônio: +R${valor:.2f}")
    
def exibir_situacao_financeira(estado):
    print("\n----- Situação Financeira -----")
    print(f"Nome: {estado['nome']}")
    print(f"Idade: {estado['idade']}")
    print(f"Profissão: {estado['profissao']}")
    print(f"Salário mensal: R${estado['salario']:.2f}")
    print(f"Patrimônio atual: R${estado['patrimonio']:.2f}")
    print(f"Dívidas atuais: R${estado['dividas']:.2f}")
    print("Histórico:")
    for evento in estado['historico']:
        print(" -", evento)
    print("------------------------------\n")