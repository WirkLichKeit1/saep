from repositories.BaseRepository import get_db
from mysql.connector import Error

class UniformeRepository:
    def getAll(self):
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM uniforme")
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return users
        except Error as e:
            print(f"Erro ao tentar buscar uniformes: {e}")
            return None

    def create(self, tamanho, numero_de_serie, vida_util):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO uniforme (tamanho, numero_de_serie, vida_util)
                VALUES
                (%s, %s, %s)
            """, (tamanho, numero_de_serie, vida_util))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print(f"Erro ao tentar criar uniforme: {e}")
            return False
    
    def update(self, tamanho, numero_de_serie, vida_util):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE uniforme SET tamanho, numero_de_serie, vida_util
            """, (tamanho, numero_de_serie, vida_util))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print(f"Erro ao tentar atualizar uniforme: {e}")
            return False