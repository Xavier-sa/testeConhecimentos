# Programa: Leitura e escrita em arquivo
# Objetivo: Receber frases do usuário, salvar em arquivo .txt e exibir o conteúdo no final

def main():
    nome_arquivo = "frases.txt"

    # Abrir o arquivo em modo escrita ('w') - sobrescreve se já existir
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        print("Digite suas frases. Digite 'sair' para encerrar.")
        while True:
            frase = input("Frase: ")
            if frase.lower() == "sair":
                break
            arquivo.write(frase + "\n")  # Escreve a frase e adiciona quebra de linha

    # Ler o arquivo e exibir o conteúdo
    print("\nConteúdo do arquivo:")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())  # remove espaços e quebras de linha extras

if __name__ == "__main__":
    main()
