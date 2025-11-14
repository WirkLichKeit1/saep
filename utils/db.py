import mysql.connector
from mysql.connector import Error

def get_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            password="",
            database="saep_db"
        )
        return conn
    except Error as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")