# Lógica de programação e algoritmos

Este guia apresenta os primeiros conceitos para você começar a resolver
problemas com programação. Leia uma seção por vez e teste os exemplos.

## Visão geral

| Item | Descrição |
| --- | --- |
| Público-alvo | Quem nunca programou ou está começando |
| Objetivo | Entender como transformar um problema em passos |
| Dificuldade | Básica |
| Tempo estimado | 30 a 45 minutos |
| Linguagem dos exemplos | Python |

---

## O que é lógica de programação?

Lógica de programação é a forma de organizar o pensamento para resolver um
problema em etapas claras.

Imagine que você quer fazer café. Você precisa seguir uma ordem:

1. Coloque água no recipiente.
2. Aqueça a água.
3. Coloque o pó no filtro.
4. Passe a água pelo pó.
5. Sirva o café.

Se você trocar a ordem ou esquecer uma etapa, o resultado pode dar errado. Um
programa funciona de maneira parecida: o computador executa as instruções na
ordem em que foram escritas.

## O que é um algoritmo?

Um **algoritmo** é uma sequência finita e organizada de passos usada para
resolver um problema.

Um bom algoritmo tem:

- um objetivo definido;
- passos claros e ordenados;
- um começo e um fim;
- um resultado esperado.

Você pode escrever um algoritmo com frases, pseudocódigo, fluxograma ou uma
linguagem de programação.

## Entrada, processamento e saída

A maioria dos programas segue três etapas:

| Etapa | O que acontece | Exemplo |
| --- | --- | --- |
| Entrada | O programa recebe um dado | O usuário informa a idade |
| Processamento | O programa trabalha com o dado | Verifica se a idade é maior ou igual a 18 |
| Saída | O programa apresenta o resultado | Mostra "Maior de idade" |

Em Python:

```python
# Entrada
idade = int(input("Digite sua idade: "))

# Processamento e saída
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

> [!NOTE]
> `input()` recebe um texto. `int()` transforma esse texto em um número inteiro.

## Formas de representar um algoritmo

### Descrição em passos

```text
1. Receber um número.
2. Dividir o número por 2.
3. Verificar o resto da divisão.
4. Se o resto for zero, informar que o número é par.
5. Caso contrário, informar que o número é ímpar.
```

### Pseudocódigo

Pseudocódigo é uma escrita simples que parece código, mas não depende de uma
linguagem específica.

```text
INÍCIO
    LEIA número

    SE número % 2 = 0 ENTÃO
        ESCREVA "O número é par"
    SENÃO
        ESCREVA "O número é ímpar"
    FIM SE
FIM
```

### Fluxograma

Um fluxograma representa os passos com formas e setas:

- **oval:** início ou fim;
- **paralelogramo:** entrada ou saída;
- **retângulo:** processamento;
- **losango:** decisão;
- **seta:** direção do fluxo.

![Fluxograma que lê um número, verifica o resto da divisão por dois e informa se ele é par ou ímpar.](diagramas/fluxo-par-impar.svg)

O arquivo-fonte do desenho está em
[`diagramas/fluxo-par-impar.mmd`](diagramas/fluxo-par-impar.mmd).

### Código Python

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```

O operador `%` calcula o resto de uma divisão. O operador `==` compara dois
valores. Não confunda `==` com `=`, que atribui um valor a uma variável.

## Conceitos fundamentais

### Variáveis

Uma variável guarda um valor para o programa usar depois.

```python
nome = "Ana"
idade = 20
altura = 1.65
estuda_python = True
```

### Tipos de dados

| Tipo | Uso | Exemplo em Python |
| --- | --- | --- |
| Inteiro (`int`) | Números sem casas decimais | `idade = 20` |
| Decimal (`float`) | Números com casas decimais | `altura = 1.65` |
| Texto (`str`) | Letras, palavras e frases | `nome = "Ana"` |
| Lógico (`bool`) | Verdadeiro ou falso | `aprovado = True` |

### Operadores

| Categoria | Operadores | Exemplo |
| --- | --- | --- |
| Aritméticos | `+`, `-`, `*`, `/`, `%` | `total = 10 + 5` |
| Comparação | `==`, `!=`, `>`, `<`, `>=`, `<=` | `idade >= 18` |
| Lógicos | `and`, `or`, `not` | `idade >= 18 and tem_documento` |

### Condicionais

Uma condicional escolhe qual caminho o programa executa.

```python
nota = 7

if nota >= 7:
    print("Aprovado")
else:
    print("Continue estudando")
```

### Repetições

Uma repetição executa uma ação várias vezes.

```python
for numero in range(1, 6):
    print(numero)
```

Esse código mostra os números de 1 a 5.

### Funções

Uma função agrupa instruções que podem ser reutilizadas.

```python
def saudacao(nome):
    return f"Olá, {nome}!"


mensagem = saudacao("Ana")
print(mensagem)
```

## Como resolver um problema

Antes de escrever o código, siga este roteiro:

1. Leia o problema com calma.
2. Identifique quais dados entram no programa.
3. Defina o resultado que o programa precisa mostrar.
4. Divida a solução em passos pequenos.
5. Escreva os passos em pseudocódigo ou desenhe um fluxograma.
6. Transforme cada passo em código.
7. Teste com valores diferentes.
8. Corrija um erro por vez.

> [!TIP]
> Faça primeiro a solução mais simples que funciona. Depois, melhore nomes,
> mensagens e organização.

## Teste de mesa

O teste de mesa simula o algoritmo no papel. Para o exemplo de par ou ímpar:

| Entrada | `numero % 2` | Condição | Saída esperada |
| --- | --- | --- | --- |
| `8` | `0` | Verdadeira | O número é par |
| `5` | `1` | Falsa | O número é ímpar |
| `0` | `0` | Verdadeira | O número é par |

Testar casos diferentes ajuda você a encontrar erros antes de considerar o
programa pronto.

## Pratique

Tente criar algoritmos para estes problemas:

1. Ler dois números e mostrar a soma.
2. Ler uma nota e informar se ela é maior ou igual a 7.
3. Mostrar os números de 1 a 10.
4. Ler três notas, calcular a média e mostrar o resultado.
5. Ler uma temperatura e informar se está frio ou quente.

Depois, compare os conceitos com os
[exercícios iniciantes](../exercicios/01_iniciante/README.md).

## Próximo passo

Escolha um exercício simples e faça três versões da solução:

1. Escreva os passos em linguagem comum.
2. Transforme os passos em pseudocódigo.
3. Implemente e teste o código em Python.

Você não precisa decorar tudo. O mais importante é praticar como dividir um
problema grande em passos menores.
