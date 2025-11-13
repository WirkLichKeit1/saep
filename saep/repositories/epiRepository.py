from repositories.BaseRepository import get_db
from mysql.connector import Error

class EpiRepository:
    def create(self, numero_de_serie, vida_util, tamanho):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO epis (numero_de_serie, vida_util, tamanho)
                VALUES
                (%s,%s,%s)
            """, (numero_de_serie, vida_util, tamanho))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print(f"Erro ao tentar criar EPI: {e}")
            return False