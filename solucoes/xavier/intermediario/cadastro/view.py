def mostrar_menu():
    print("===== MENU =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    return input("Escolha uma opção: ")

def pedir_dados_usuario():
    nome = input("Informe o nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))
    return nome, idade

def mostrar_usuarios(usuarios):
    if not usuarios:
        print(" Nenhum usuário cadastrado.\n")
        return

    print("\n Lista de usuários cadastrados:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i} - Nome: {u['nome']} | Idade: {u['idade']}")
    print()
