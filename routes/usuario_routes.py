from flask import Flask, jsonify,Blueprint,  request
from conexao import conecta_db

from bd.usuario import listar_usuarios_bd, inserir_usuario_bd

usuario_bp = Blueprint("usuario", __name__, url_prefix= "/usuarios")

@usuario_bp.route("/", methods=["GET"])
def listar_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuarios_bd(conexao)
    return jsonify(usuarios)

@usuario_bp.route("/", methods=["POST"])
def salvar_usuario():
    conexao = conecta_db()
    dados  = request.get_json()
    
    login  = dados['login']
    senha  = dados['senha']
    admin  = dados['admin']
    
    inserir_usuario_bd(conexao,login,senha,admin)
    return jsonify({"message":"Usuário salvo com sucesso !"})
