import os
import pytest
import services
from flask import Flask
from routes import main_routes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "src", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "src", "static")


@pytest.fixture(autouse=True)
def limpar_tarefas():
    services.tarefas.clear()
    yield
    services.tarefas.clear()


@pytest.fixture
def client():
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
    app.register_blueprint(main_routes)
    return app.test_client()


def test_criar_tarefa_adiciona_na_lista():
    tarefa = services.criar_tarefa("Estudar Java", "Ler a documentação oficial", "alta")

    assert tarefa["titulo"] == "Estudar Java"
    assert tarefa["status"] == "pendente"
    assert len(services.tarefas) == 1


def test_listar_tarefas_retorna_dados_formatados():
    services.criar_tarefa("Tarefa 1", "Descrição 1", "alta")

    tarefas = services.listar_tarefas()

    assert tarefas[0]["prioridade"] == "Alta"
    assert tarefas[0]["prioridade_class"] == "alta"
    assert tarefas[0]["status"] == "Pendente"


def test_buscar_tarefa_existente():
    services.criar_tarefa("Tarefa 1", "Descrição 1", "media")

    tarefa = services.buscar_tarefa(1)

    assert tarefa is not None
    assert tarefa["titulo"] == "Tarefa 1"


def test_buscar_tarefa_inexistente_retorna_none():
    assert services.buscar_tarefa(999) is None


def test_editar_tarefa_existente_atualiza_os_dados():
    services.criar_tarefa("Tarefa original", "Descrição original", "baixa")

    resultado = services.editar_tarefa(1, "Tarefa editada", "Descrição editada", "alta")
    tarefa = services.buscar_tarefa(1)

    assert resultado is True
    assert tarefa["titulo"] == "Tarefa editada"
    assert tarefa["prioridade_class"] == "alta"


def test_editar_tarefa_inexistente_retorna_false():
    assert services.editar_tarefa(999, "X", "Y", "alta") is False


def test_excluir_tarefa_existente():
    services.criar_tarefa("Tarefa a excluir", "Descrição", "media")

    resultado = services.excluir_tarefa(1)

    assert resultado is True
    assert services.buscar_tarefa(1) is None


def test_excluir_tarefa_inexistente_retorna_false():
    assert services.excluir_tarefa(999) is False


#testes de rota 

def test_pagina_inicial_sem_tarefas_mostra_estado_vazio(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert "Nenhuma tarefa cadastrada".encode("utf-8") in resposta.data


def test_post_create_cria_tarefa_e_redireciona_para_lista(client):
    resposta = client.post(
        "/create",
        data={"titulo": "Nova tarefa", "descricao": "Descrição", "prioridade": "alta"},
        follow_redirects=True,
    )

    assert resposta.status_code == 200
    assert "Nova tarefa".encode("utf-8") in resposta.data


def test_editar_tarefa_com_id_inexistente_retorna_404(client):
    resposta = client.get("/edit/999")

    assert resposta.status_code == 404