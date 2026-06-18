tarefas = []

PRIORIDADES = {
    "alta": "Alta",
    "media": "Média",
    "baixa": "Baixa",
}

STATUS = {
    "pendente": "Pendente",
    "andamento": "Em andamento",
    "concluida": "Concluída",
}


def _buscar_bruta(id_tarefa):

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None


def _formatar_tarefa(tarefa):

    tarefa_formatada = tarefa.copy()
    tarefa_formatada["prioridade_class"] = tarefa["prioridade"]
    tarefa_formatada["prioridade"] = PRIORIDADES.get(tarefa["prioridade"], tarefa["prioridade"])
    tarefa_formatada["status_class"] = tarefa["status"]
    tarefa_formatada["status"] = STATUS.get(tarefa["status"], tarefa["status"])
    return tarefa_formatada


def listar_tarefas():
    return [_formatar_tarefa(tarefa) for tarefa in tarefas]


def buscar_tarefa(id_tarefa):
    tarefa = _buscar_bruta(id_tarefa)

    if tarefa is None:
        return None

    return _formatar_tarefa(tarefa)


def criar_tarefa(titulo, descricao, prioridade):

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "pendente",
    }

    tarefas.append(nova_tarefa)

    return nova_tarefa


def editar_tarefa(id_tarefa, titulo, descricao, prioridade):

    tarefa = _buscar_bruta(id_tarefa)

    if tarefa is None:
        return False

    tarefa["titulo"] = titulo
    tarefa["descricao"] = descricao
    tarefa["prioridade"] = prioridade

    return True


def excluir_tarefa(id_tarefa):

    tarefa = _buscar_bruta(id_tarefa)

    if tarefa is None:
        return False

    tarefas.remove(tarefa)

    return True