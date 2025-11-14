from utils.db import get_db
from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

def get_by_email(email):
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = (%s)", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    except Error as e:
        print(f"Erro ao tentar buscar usuario pelo email: {e}")
        return None

def getAll():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM itens")
        itens = cursor.fetchall()
        cursor.close()
        conn.close()
        return itens
    except Error as e:
        print(f"Erro ao tentar buscar itens: {e}")
        return None

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")
    if not all([email, senha]):
        return jsonify({"error": "Campos obrigatorios"}), 400
    
    user = get_by_email(email)
    if not user:
        return jsonify({"error": "Email invalido"}), 401
    
    return jsonify({"user": user}), 200

@app.route("/itens", methods=["GET"])
def itens():
    return jsonify({"itens": getAll()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)