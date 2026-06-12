# TechFlow Task Manager

## 📋 Sobre o Projeto

O **TechFlow Task Manager** é um sistema web simples para gerenciamento de tarefas, desenvolvido como parte da atividade prática da disciplina de Engenharia de Software.

O projeto simula uma solução criada pela empresa fictícia **TechFlow Solutions** para atender uma startup do setor de logística que necessita acompanhar o fluxo de trabalho da equipe em tempo real, organizar prioridades e melhorar a produtividade utilizando conceitos de metodologias ágeis.

---

## 🎯 Objetivo

Desenvolver um sistema básico de gerenciamento de tarefas aplicando conceitos de:
- Engenharia de Software;
- Metodologias Ágeis (Kanban);
- Controle de versão com Git e GitHub;
- Testes automatizados;
- Integração Contínua (CI) utilizando GitHub Actions.

---

## 🚀 Funcionalidades

- ✅ Cadastro de tarefas;
- ✅ Visualização da lista de tarefas;
- ✅ Edição de tarefas;
- ✅ Exclusão de tarefas;
- ✅ Definição de prioridade das tarefas (implementada como alteração de escopo do projeto);
- ✅ Testes automatizados;
- ✅ Pipeline de integração contínua com GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Pytest
- Git e GitHub
- GitHub Projects (Kanban)
- GitHub Actions

---

## 📂 Estrutura do Projeto

```text
src/            -> Código-fonte da aplicação
tests/          -> Testes automatizados
docs/           -> Diagramas UML e documentação complementar
.github/        -> Configuração do GitHub Actions
templates/      -> Interfaces HTML
static/         -> Arquivos CSS
```

---

## 📌 Metodologia Ágil Utilizada

O projeto foi organizado utilizando a metodologia **Kanban**, através do GitHub Projects, permitindo o acompanhamento do fluxo de desenvolvimento por meio das colunas:
- To Do;
- In Progress;
- Done.

As atividades foram divididas em tarefas menores e acompanhadas durante todo o ciclo de desenvolvimento.

---

## 🔄 Gestão de Mudanças

### Alteração de Escopo

Durante o desenvolvimento, foi simulada uma solicitação do cliente para incluir uma nova funcionalidade: **classificação das tarefas por nível de prioridade (Alta, Média e Baixa)**.

A alteração foi registrada no quadro Kanban, implementada no sistema e documentada neste repositório, demonstrando a flexibilidade das metodologias ágeis para adaptação a novas necessidades.

---

## 🧪 Testes Automatizados

O projeto utiliza **Pytest** para validação das funcionalidades básicas da aplicação. Os testes são executados automaticamente por meio do **GitHub Actions** sempre que há uma atualização no repositório.

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/luisAzeve/techflow-task-manager.git
```

### 2. Acesse a pasta do projeto

```bash
cd techflow-task-manager
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python src/app.py
```

### 5. Execute os testes

```bash
pytest
```

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos, como atividade prática da disciplina de Engenharia de Software.
