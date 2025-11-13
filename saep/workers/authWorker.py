from flask import jsonify
from repositories.funcionarioRepository import FuncionarioRepository

repo = FuncionarioRepository()

class AuthWorker:
    def login(self, nome):
        user = repo.get_by_nome(nome)
        if not user:
            return jsonify({"error": "nome invalido"}), 401
        
        return jsonify({
            "user": user["nome"]
        })