from model import adicionar_usuario, obter_usuarios
import view

def executar():
    while True:
        opcao = view.mostrar_menu()

        if opcao == "1":
            nome, idade = view.pedir_dados_usuario()
            adicionar_usuario(nome, idade)
            print(" Usuário cadastrado com sucesso!\n")

        elif opcao == "2":
            view.mostrar_usuarios(obter_usuarios())

        elif opcao == "3":
            print(" Encerrando o programa...")
            break
        else:
            print(" Opção inválida.\n")
