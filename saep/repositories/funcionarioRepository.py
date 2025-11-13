from repositories.BaseRepository import get_db
from mysql.connector import Error

class FuncionarioRepository:
    def create(self, nome):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO funcionario (nome) VALUES (%s)", (nome,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print(f"Erro ao tentar criar funcionario: {e}")
            return False
    
    def get_by_nome(self, nome):
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM funcionario WHERE nome = (%s)", (nome,))
            func = cursor.fetchone()
            cursor.close()
            conn.close()
            return func
        except Error as e:
            print(f"Erro ao tentar buscar pelo nome: {e}")
            return False