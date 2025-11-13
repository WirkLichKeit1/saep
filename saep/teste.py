from utils._db import get_db

def teste():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for t in tables:
            print("-", t[0])
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro: {e}")

teste()