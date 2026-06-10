# Primeiro Contato com Git, GitHub e Python

<!--
  Objetivo deste arquivo:
  Servir como um passo a passo simples para ajudar quem está começando a entender:
  1. O que é Git.
  2. O que é GitHub.
  3. Como criar um repositório.
  4. Como criar um primeiro arquivo Python.
  5. Como enviar o projeto para o GitHub.
-->

## Visão Geral

| Item | Descrição |
| --- | --- |
| Público-alvo | Quem está começando em programação |
| Objetivo | Criar um primeiro projeto Python e enviar para o GitHub |
| Dificuldade | Básica |
| Tempo estimado | 40 a 60 minutos |
| Resultado final | Um repositório no GitHub com um arquivo Python |

---

## Legenda do Guia

- `Execute`: etapa prática para fazer no computador.
- `Dica de ensino`: orientação para quem está ensinando.
- `Atenção`: cuidado importante antes de seguir.
- `Erro comum`: problema frequente que deve ser evitado.

---

## Antes de Começar

Você vai precisar de:

- Um computador com acesso à internet.
- Um e-mail válido.
- Um navegador instalado.
- O Git instalado no computador.
- Um editor de código, como Visual Studio Code.

> [!NOTE]
> Dica de ensino: se você estiver guiando alguém no primeiro contato, não misture muitos assuntos no mesmo dia. O foco é entender o caminho básico: computador, Git, GitHub.

---

## Passo 1 - Entender o Que é Git e GitHub

### O que é Git?

Git é uma ferramenta instalada no computador para controlar versões do código.

Com Git, você consegue:

- Salvar mudanças importantes.
- Voltar para uma versão anterior.
- Acompanhar o histórico do projeto.
- Trabalhar em equipe com mais segurança.

### O que é GitHub?

GitHub é um site onde você guarda repositórios Git na nuvem.

### Analogia simples

| Conceito | Analogia |
| --- | --- |
| Git | Caderno de anotações do projeto |
| GitHub | Armário online onde o caderno fica guardado |
| Repositório | Pasta principal do projeto |
| Commit | Um ponto salvo no histórico |

> [!NOTE]
> Dica de ensino: comece pelas analogias e depois mostre os comandos. Para quem está começando, entender o conceito antes do terminal costuma funcionar melhor.

---

## Passo 2 - Criar uma Conta no GitHub

**Execute:**

1. Acesse: <https://github.com>
2. Clique em `Sign up`.
3. Informe e-mail, senha e nome de usuário.
4. Confirme a conta pelo e-mail.
5. Faça login no GitHub.

> [!WARNING]
> Atenção: guarde o e-mail usado no cadastro. Ele será usado também na configuração do Git.

---

## Passo 3 - Criar o Primeiro Repositório

Depois de entrar no GitHub:

1. Clique em `New repository`.
2. Escolha um nome simples, por exemplo:

```text
aprendendo-python
```

3. Não marque a opção `Add a README file`.
4. Clique em `Create repository`.

### O que é um repositório?

Um repositório é a pasta principal do projeto. Tudo que você desenvolver ficará organizado ali.

> [!IMPORTANT]
> Neste primeiro contato, criar o repositório vazio evita conflitos quando o projeto local for enviado para o GitHub.

> [!NOTE]
> Dica de ensino: neste momento, não precisa explicar branch, merge ou pull request. Primeiro ajude quem está aprendendo a ficar confortável com repositório e commit.

---

## Passo 4 - Instalar o Git

**Execute:**

1. Acesse: <https://git-scm.com/downloads>
2. Baixe a versão para o seu sistema operacional.
3. Instale mantendo as opções padrão.
4. Abra o terminal.
5. Teste se o Git foi instalado:

```bash
git --version
```

Se aparecer uma versão, por exemplo `git version 2.45.0`, a instalação funcionou.

> [!CAUTION]
> Erro comum: se o comando não funcionar, feche e abra o terminal novamente. Em muitos casos o terminal só precisa recarregar a configuração.

---

## Passo 5 - Configurar o Git no Computador

Essa configuração identifica quem está salvando as mudanças no projeto.

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@email.com"
```

Para conferir se funcionou:

```bash
git config --global --list
```

O resultado deve mostrar algo parecido com:

```text
user.name=Seu Nome
user.email=seu-email@email.com
```

> [!WARNING]
> Atenção: use o mesmo e-mail da conta do GitHub para facilitar a identificação dos commits.

---

## Passo 6 - Criar o Primeiro Projeto Python

Crie uma pasta no computador e entre nela:

```bash
mkdir aprendendo-python
cd aprendendo-python
```

Dentro dela, crie um arquivo chamado:

```text
main.py
```

Adicione este código:

```python
nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")
```

### Explicação simples

No Python, você não precisa declarar o tipo da variável como em C, Java ou C#.

Exemplo:

```python
idade = 18
```

O Python identifica automaticamente que `idade` é um número inteiro.

Outro exemplo:

```python
nome = "Ana"
```

O Python identifica automaticamente que `nome` é um texto.

> [!NOTE]
> Dica de ensino: este é um bom momento para explicar entrada, processamento e saída. Você digita o nome, o programa guarda na variável e depois imprime uma mensagem.

---

## Passo 7 - Rodar o Programa Python

No terminal, entre na pasta do projeto e execute:

```bash
python main.py
```

Se o computador usar `python3`, execute:

```bash
python3 main.py
```

O programa deve pedir:

```text
Digite seu nome:
```

Depois deve responder:

```text
Olá, NomeDigitado!
```

---

## Passo 8 - Salvar o Projeto com Git

Dentro da pasta do projeto, execute:

```bash
git init
git status
git add .
git commit -m "Primeiro commit"
```

### O que cada comando faz?

| Comando | Função |
| --- | --- |
| `git init` | Inicia o Git na pasta |
| `git status` | Mostra o estado dos arquivos |
| `git add .` | Prepara os arquivos para salvar |
| `git commit -m "Primeiro commit"` | Salva um ponto no histórico |

> [!WARNING]
> Atenção: commit não envia automaticamente para o GitHub. Commit salva no histórico local do computador.

---

## Passo 9 - Conectar o Projeto ao GitHub

No GitHub, copie a URL do repositório criado.

Ela será parecida com:

```text
https://github.com/seu-usuario/aprendendo-python.git
```

No terminal, execute:

```bash
git remote add origin URL_DO_REPOSITORIO
git branch -M main
git push -u origin main
```

Exemplo:

```bash
git remote add origin https://github.com/seu-usuario/aprendendo-python.git
git branch -M main
git push -u origin main
```

> [!CAUTION]
> Erro comum: não copie o exemplo exatamente como está. Troque `seu-usuario` pelo seu nome de usuário real do GitHub.

---

## Passo 10 - Conferir no GitHub

Volte ao repositório no GitHub e atualize a página.

Você deve ver:

- O arquivo `main.py`.
- O arquivo `README.md`, caso você tenha criado esse arquivo.
- O histórico com o commit `Primeiro commit`.

> [!TIP]
> Concluído: neste ponto, você já criou um projeto Python, salvou com Git e enviou para o GitHub.

---

## Ordem Recomendada para Ensinar

1. O que é programação.
2. O que é Git.
3. O que é GitHub.
4. Como criar uma conta no GitHub.
5. Como criar um repositório.
6. Como instalar o Git.
7. Como configurar nome e e-mail.
8. Como criar um arquivo Python simples.
9. Como fazer commits.
10. Como enviar o projeto para o GitHub.

---

## O Que Evitar no Primeiro Dia

Evite explicar estes assuntos logo no início:

- Branch.
- Merge.
- Pull request.
- Rebase.
- Conflitos complexos.
- GitHub Actions.
- Deploy.

> [!WARNING]
> Dica de ensino: esses assuntos são importantes, mas podem confundir quem ainda está entendendo arquivo, pasta, terminal, Git e GitHub.

---

## Resumo Final

O caminho principal é:

```text
Computador -> Git -> GitHub
```

E a rotina básica é:

```bash
git status
git add .
git commit -m "Mensagem do commit"
git push
```

Quando você entender essa rotina, já terá uma base sólida para continuar aprendendo Git, GitHub e programação.
