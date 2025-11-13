from repositories.BaseRepository import get_db
from mysql.connector import Error

class HistoricoRepository:
    def create(self, funcionario_id, uniforme_id, epi_id):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO historico (funcionario_id, uniforme_id, epi_id)
                VALUES
                (%s,%s,%s)
            """, (funcionario_id, uniforme_id, epi_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print(f"Erro ao tentar criar historico: {e}")
            return False
        
    def getById(self, fun_id):
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM historico WHERE id = (%s)", (fun_id,))
            his = cursor.fetchall()
            cursor.close()
            conn.close()
            return his
        except Error as e:
            print(f"Erro ao tentar buscar historico: {e}")
            return None