# 🐍 Repositório de Prática em Python

Este repositório foi criado para que os membros do time desenvolvam suas habilidades em Python através de exercícios práticos e colaborativos.

## 📋 Sobre

O objetivo deste projeto é fornecer um ambiente estruturado onde cada membro pode:
- Praticar conceitos fundamentais de Python
- Resolver exercícios de diferentes níveis de dificuldade
- Acompanhar o progresso individual
- Colaborar de forma organizada usando Git/GitHub

## 🗂️ Estrutura do Repositório

```
├── exercicios/          # Lista de exercícios disponíveis
├── solucoes/           # Diretório para soluções (organizado por membro)
│   ├── wendril/
│   ├── xavier/
│   ├── matheus/
│   ├── rodrigo/
│   └── samuel/
├── recursos/           # Material de apoio e referências
└── README.md          # Este arquivo
```

## 👥 Membros da Equipe

| Nome | GitHub | Branch |
|------|--------|--------|
| Wendril | [@WendrilSFS](https://github.com/WendrilSFS) | `wendril-exercicios` |
| Xavier | [@Xavier-sa](https://github.com/Xavier-sa) | `xavier-testeXavier-feature/01` |
| Matheus | [@matheuscorsine](https://github.com/matheuscorsine) | `matheus-exercicios` |
| Rodrigo | [@rodrigo570282](https://github.com/rodrigo570282) | `rodrigo-exercicios` |
| Samuel | [@samuelserri](https://github.com/samuelserri) | `samuel-exercicios` |

## 🚀 Como Começar

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd repositorio-python-pratica
```

### 2. Crie sua branch pessoal
```bash
git checkout -b seu-nome-exercicios
```

### 3. Configure seu ambiente
```bash
# Exemplo de estrutura para suas soluções
mkdir solucoes/seu-nome
cd solucoes/seu-nome
```

### 4. Trabalhe nos exercícios
- Consulte a pasta `exercicios/` para ver os desafios disponíveis
- Desenvolva suas soluções na sua pasta pessoal
- Faça commits regulares com mensagens descritivas

### 5. Envie suas soluções
```bash
git add .
git commit -m "feat: adiciona solução do exercício X"
git push origin seu-nome-exercicios
```

## 📝 Convenções de Commit

Para manter o histórico organizado, use as seguintes convenções:

- `feat:` Nova solução ou funcionalidade
- `fix:` Correção de bug ou erro
- `docs:` Documentação ou comentários
- `refactor:` Melhoria no código existente
- `test:` Adição de testes

**Exemplos:**
```bash
git commit -m "feat: solução do exercício de listas"
git commit -m "fix: corrige lógica do algoritmo de ordenação"
git commit -m "docs: adiciona comentários explicativos"
```

## 📚 Lista de Exercícios

### Nível Iniciante
- [ ] Calculadora básica
- [ ] Conversor de temperaturas  
- [ ] Contador de palavras
- [ ] Jogo de adivinhação

### Nível Intermediário
- [ ] Sistema de notas
- [ ] Gerenciador de tarefas
- [ ] Análise de dados simples
- [ ] API básica com Flask

### Nível Avançado
- [ ] Web scraping
- [ ] Machine Learning básico
- [ ] Processamento de imagens
- [ ] Sistema de banco de dados

## 🎯 Regras de Colaboração

### ✅ Boas Práticas
- Mantenha sua branch sempre atualizada com a `main`
- Escreva código limpo e bem comentado
- Use nomes descritivos para variáveis e funções
- Inclua docstrings nas suas funções
- Teste suas soluções antes de fazer commit

### ❌ Evitar
- Trabalhar diretamente na branch `main`
- Commits sem mensagens descritivas
- Código sem comentários ou documentação
- Pushing de arquivos desnecessários (cache, etc.)

## 🔄 Fluxo de Trabalho

1. **Sincronize** sua branch com as atualizações da main:
   ```bash
   git checkout main
   git pull origin main
   git checkout sua-branch
   git merge main
   ```

2. **Desenvolva** sua solução

3. **Teste** o código completamente

4. **Commit** com mensagem clara

5. **Push** para sua branch remota

6. **Abra um Pull Request** quando quiser feedback (opcional)

## 🆘 Precisa de Ajuda?

- 📖 Consulte a pasta `recursos/` para materiais de apoio
- 💬 Abra uma [issue](../../issues) para dúvidas específicas
- 🤝 Peça ajuda aos outros membros da equipe

## 📊 Acompanhamento de Progresso

Cada membro pode acompanhar seu progresso usando a checklist nos exercícios e mantendo um registro pessoal na sua pasta de soluções.

---

**Lembre-se:** O objetivo não é apenas resolver os exercícios, mas aprender e melhorar suas habilidades de programação. Não hesite em experimentar, errar e aprender!

Happy coding! 🎉