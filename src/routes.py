from flask import Blueprint, render_template

main_routes =  Blueprint('main', __name__)

@main_routes.route("/")
def pagina_inicial():
    return render_template("index.html")

@main_routes.route("/create")
def criar_tarefa():
    return render_template("create.html")