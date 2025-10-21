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

if __name__ == "__main__":
    coletar_dados()
