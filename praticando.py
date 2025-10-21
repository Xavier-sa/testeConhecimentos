#praticando o basico 
def coletar_dados(numero=12, entrada_func=input):
    """
    Coleta dados do usuário e inicializa o estado financeiro.
    Retorna o dicionário de estado inicial ou None em caso de erro de entrada.
    """
    dados = [] #

    try:
        nome = entrada_func("NOME:")
        idade = int(entrada_func("IDADE:"))
        profissao = entrada_func("PROFISSÃO:")
        salario = float(entrada_func("SALARIO:"))
    except ValueError:
        print("[ERRO] Idade e Salário devem ser números válidos.")
        return None

    # Inicialização do estado (Patrimônio inicial assumido como 1 ano de salário)
    patrimonio_inicial = salario * 12
    
    estado_inicial = {
        "numero": numero,
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "salario": salario,
        "patrimonio": patrimonio_inicial,
        "dividas": 0.0,
        "historico": [f"Situação inicial. Patrimônio baseado em 1 ano de salário: R${patrimonio_inicial:.2f}"]
    }

    
    dados.append({
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "salario": salario,
        "numero": numero
    })

    #
    print(f"""
O player nº{numero} {'-'*20}

Nickname: {nome} {'-'*20}

Tem a idade de {idade} {'-'*20}

Sua Ocupação é {profissao} {'-'*20}

Possui um salario de {salario:.2f}
""")
    
    return estado_inicial
    
def emprestimo(estado, valor, juros=0.02):
    """Simula a aquisição de um empréstimo."""
    print(f"Solicitando empréstimo de R${valor:.2f} com juros de {juros*100:.1f}%")
    estado['dividas'] += valor * (1 + juros)
    estado['patrimonio'] += valor
    estado['historico'].append(f"Empréstimo: +R${valor:.2f}, dívida aumentou para R${estado['dividas']:.2f}")
    print("Empréstimo concedido.")
    
    
def financiamento(estado, valor, juros=0.015):
    """Simula a aquisição de um financiamento."""
    print(f"Financiando bem no valor de R${valor:.2f} com juros de {juros*100:.1f}%")
    estado['dividas'] += valor * (1 + juros)
    estado['patrimonio'] += valor
    estado['historico'].append(f"Financiamento: +R${valor:.2f}, dívida aumentou para R${estado['dividas']:.2f}")
    print("Financiamento aprovado.")
    
    
def alienacao(estado, valor):
    """Simula a venda de um ativo para pagar dívidas."""
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
    """Simula o aumento direto do patrimônio (ex: investimentos)."""
    print(f"Aumentando patrimônio em R${valor:.2f}")
    estado['patrimonio'] += valor
    estado['historico'].append(f"Aumento patrimônio: +R${valor:.2f}")
    
def exibir_situacao_financeira(estado):
    """Exibe o resumo financeiro atual do estado."""
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
    
    
def simular_trilha_riqueza(entrada_func=input):
    """Função principal para rodar a simulação."""
    print("--- INÍCIO DA SIMULAÇÃO DE TRILHA DE RIQUEZA ---")
    
    estado = coletar_dados(entrada_func=entrada_func)
    if estado is None:
        print("Simulação encerrada devido a entrada inválida.")
        return

    exibir_situacao_financeira(estado)

    print("--- Realizando Ações Financeiras ---")
    emprestimo(estado, 5000)
    financiamento(estado, 15000)
    alienacao(estado, 7000)
    elevacao_patrimonio(estado, 2000)
    print("--- FIM DAS AÇÕES ---\n")
    
    exibir_situacao_financeira(estado)
    
    
if __name__ == "__main__":
        simular_trilha_riqueza()