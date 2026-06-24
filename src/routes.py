from flask import Blueprint, render_template, request, redirect, url_for, abort
import services

main_routes = Blueprint('main', __name__)


@main_routes.route("/")
def pagina_inicial():
    tarefas = services.listar_tarefas()
    return render_template("index.html", tasks=tarefas)


@main_routes.route("/create", methods=["GET", "POST"])
def criar_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        prioridade = request.form.get("prioridade")

        services.criar_tarefa(titulo, descricao, prioridade)
        return redirect(url_for("main.pagina_inicial"))

    return render_template("create.html")


@main_routes.route("/edit/<int:id_tarefa>", methods=["GET", "POST"])
def editar_tarefa(id_tarefa):
    tarefa = services.buscar_tarefa(id_tarefa)

    if tarefa is None:
        abort(404)

    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        prioridade = request.form.get("prioridade")
        status = request.form.get("status")

        services.editar_tarefa(id_tarefa, titulo, descricao, prioridade, status)
        return redirect(url_for("main.pagina_inicial"))

    return render_template("edit.html", task=tarefa)


@main_routes.route("/excluir/<int:id_tarefa>", methods=["POST"])
def excluir_tarefa(id_tarefa):
    services.excluir_tarefa(id_tarefa)
    return redirect(url_for("main.pagina_inicial"))