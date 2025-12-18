from flask import Flask, jsonify, request, Blueprint

from categoria_repository import CategoriaRepository
from categoria import Categoria
import categoria_repository

categoria_bp = Blueprint("categoria", __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    repo = CategoriaRepository()
    # dados = [dict()]
    dados = repo.find_all()
    dicionario = []
    # cabecalhos = ['id','nome','descricao']
    # dados_retorno = [dict(zip(cabecalhos,d))for d in dados]
    for dado in dados:
        dicionario.append({'id':dado[0],'nome':dado[1],'descricao':dado[2]})
    return jsonify(dicionario)

@categoria_bp.route('/categorias/<int:catregoriaID>')
def buscar_id(catregoriaID):
    repo = CategoriaRepository()
    categoria = repo.find_by_id(catregoriaID)
    categoria_retorno = {'id':categoria[0], 'nome':categoria[1],'descricao':categoria[2]}
    return jsonify(categoria_retorno)

@categoria_bp.route('/categorias', methods = ['POST'])
def cadastrar_categoria():
    repo = CategoriaRepository()

    dados_json = request.get_json()
    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")

    repo.create(nome, descricao)

    return jsonify({"Mensagem":"Categoria cadastrada com sucesso.",
                    "nome":nome,
                    "descricao":descricao}),201

@categoria_bp.route('/categorias/<int:id_categoria>', methods=['DELETE'])
def remover_categoria(id_categoria):
    repo = CategoriaRepository()

    repo.delete(id_categoria)
    return jsonify({
        "mensagem": "Categoria removida com sucesso."
    })


