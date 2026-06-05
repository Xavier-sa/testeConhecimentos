"""
Exercicio 23 - Liberacao de acesso ao sistema financeiro

Um usuario podera acessar o sistema financeiro se:
- possuir login ativo
- possuir autenticacao em dois fatores
- possuir permissao do setor financeiro

Analistas financeiros podem acessar sem autorizacao extra.

Nenhum usuario podera acessar se estiver com senha expirada.
"""

print("23. Liberacao de Acesso ao Sistema Financeiro")

senha_expirada = input("A senha esta expirada? (s/n): ") == "s"

if senha_expirada:
    print("Resultado: Acesso Negado. Senha expirada.")
else:
    login_ativo = input("Login ativo? (s/n): ") == "s"

    if not login_ativo:
        print("Resultado: Acesso Negado. Login inativo.")
    else:
        dois_fatores = input("Autenticacao em dois fatores ativada? (s/n): ") == "s"

        if not dois_fatores:
            print("Resultado: Acesso Negado. Autenticacao em dois fatores obrigatoria.")
        else:
            analista = input("E analista financeiro? (s/n): ") == "s"

            if analista:
                print("Resultado: Acesso Permitido. Analista financeiro.")
            else:
                permissao = input("Possui permissao do setor financeiro? (s/n): ") == "s"

                if permissao:
                    print("Resultado: Acesso Permitido.")
                else:
                    print("Resultado: Acesso Negado. Permissao financeira ausente.")
