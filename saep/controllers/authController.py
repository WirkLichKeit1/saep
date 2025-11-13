from flask import Blueprint, jsonify, request
from workers.authWorker import AuthWorker

worker = AuthWorker()

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nome = data.get("nome")
    if not nome:
        return jsonify({"error": "Campos obrigatorios"}), 400
    return worker.login(nome)