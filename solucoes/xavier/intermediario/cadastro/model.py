
usuarios = []

def adicionar_usuario(nome, idade):
    usuario = {"nome": nome, "idade": idade}
    usuarios.append(usuario)

def obter_usuarios():
    return usuarios
