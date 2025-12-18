from flask import Flask, jsonify, request, Blueprint
from produto_repository import ProdutoRepository
from produto import Produto
import produto_repository

produto_bp = Blueprint("produto", __name__)

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    repo = ProdutoRepository()

    dados = repo.find_all()
    dicionario = []

    for dado in dados:
        dicionario.append({'id':dado[0],'nome':dado[1],'descricao':dado[2],'preco':dado[3],'quantidadeEstoque': dado[4], 'categoriaID': dado[5]})
    return jsonify(dicionario)

@produto_bp.route('/produtos/<int:ProdutoID>')
def buscar_id(ProdutoID):
    repo = ProdutoRepository()
    categoria = repo.find_by_id(ProdutoID)
    categoria_retorno = {'id':categoria[0], 'nome':categoria[1],'descricao':categoria[2],'preco':categoria[3],'quantidadeEstoque': categoria[4], 'categoriaID': categoria[5]}
    return jsonify(categoria_retorno)

@produto_bp.route('/produtos', methods = ['POST'])
def cadastrar_produtos():
    repo = ProdutoRepository()

    dados_json = request.get_json()
    # id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")
    preco = dados_json.get("preco")
    qtd_estoque = dados_json.get("qtd_estoque")
    categoria_id = dados_json.get("categoriaID")

    repo.create(nome, descricao,preco,qtd_estoque,categoria_id)

    return jsonify({"Mensagem":"Produto cadastrada com sucesso.",
                    "nome":nome,
                    "descricao":descricao,
                    "preco": preco,
                    "qtd_estoque":qtd_estoque,
                    "categoriaID": categoria_id}),201

# @app.route('/categorias/<int:id_categoria>', methods=['DELETE'])
# def remover_categoria(id_categoria):
#     repo = CategoriaRepository()

#     repo.delete(id_categoria)
#     return jsonify({
#         "mensagem": "Categoria removida com sucesso."
#     })


