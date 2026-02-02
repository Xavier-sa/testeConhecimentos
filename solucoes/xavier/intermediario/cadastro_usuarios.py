
usuarios = []

def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))

    usuario = {
        "nome": nome,
        "idade": idade
    }
    usuarios.append(usuario)
    print(" Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print(" Nenhum usuário cadastrado.\n")
        return

    print("\n Lista de usuários cadastrados:")
    for i in range(len(usuarios)):
        print(f"{i + 1} - Nome: {usuarios[i]['nome']} | Idade: {usuarios[i]['idade']}")
    print()

def menu():
    while True:
        print("===== MENU =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print(" Encerrando o programa...")
            break
        else:
            print(" Opção inválida. Tente novamente.\n")



menu()
