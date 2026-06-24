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
- ✅ Classificação de tarefas por nível de prioridade (Alta, Média e Baixa) — implementada como alteração de escopo;
- ✅ Testes automatizados;
- ✅ Pipeline de integração contínua com GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Flask
- Pytest
- Git e GitHub
- GitHub Projects (Kanban)
- GitHub Actions

---

## 📂 Estrutura do Projeto

```text
techflow-task-manager/
├── .github/workflows/   -> Pipeline de integração contínua (GitHub Actions)
├── docs/                -> Diagramas UML e documentação complementar
├── src/
│   ├── static/          -> Arquivos CSS
│   ├── templates/       -> Interfaces HTML (Jinja2)
│   ├── app.py           -> Inicialização do servidor Flask
│   ├── routes.py        -> Definição das rotas da aplicação
│   ├── services.py      -> Lógica de negócio e gerenciamento de dados
│   └── models.py        -> Definição da estrutura de dados
├── tests/               -> Testes automatizados com Pytest
├── conftest.py          -> Configuração do ambiente de testes
└── requirements.txt     -> Dependências do projeto
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

Durante o desenvolvimento, foi identificada a necessidade de incluir uma nova funcionalidade não prevista no escopo inicial: a **classificação das tarefas por nível de prioridade (Alta, Média e Baixa)**.

A solicitação partiu do cliente, que precisava distinguir tarefas críticas das demais para melhor organizar o fluxo de trabalho da equipe.

**Como a mudança foi gerenciada:**

1. Um novo card foi criado no quadro Kanban (GitHub Projects) descrevendo a funcionalidade;
2. O card passou pelas colunas To Do → In Progress → Done conforme o desenvolvimento avançou;
3. A funcionalidade foi implementada na camada de serviço (`services.py`) e refletida nas telas de criação e edição de tarefas;
4. Um novo commit foi registrado documentando a mudança.

---

## 🧪 Testes Automatizados

O projeto utiliza **Pytest** para validação das funcionalidades da aplicação. São 11 testes organizados em dois grupos:

- **Testes de serviço:** validam as operações de criar, listar, buscar, editar e excluir tarefas diretamente na camada de lógica (`services.py`), incluindo cenários de erro (ex: editar ou excluir uma tarefa que não existe);
- **Testes de rota:** validam o comportamento das rotas HTTP, como o retorno correto de páginas e o tratamento de requisições com dados inválidos (ex: acessar `/edit/999` retorna 404).

Os testes são executados automaticamente pelo **GitHub Actions** a cada `push` na branch `main`.

---

## ⚙️ Integração Contínua (CI)

O pipeline configurado em `.github/workflows/ci.yml` executa automaticamente os seguintes passos a cada atualização no repositório:

1. Checkout do código;
2. Configuração do Python 3.12;
3. Instalação das dependências via `requirements.txt`;
4. Execução dos testes com `pytest -v`.

Se todos os testes passarem, o commit recebe um ✅. Caso algum falhe, o commit recebe um ❌ e a equipe é notificada.

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

Projeto desenvolvido para fins acadêmicos, como atividade prática da disciplina de Engenharia de Software — UniFECAF.