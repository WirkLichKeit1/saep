import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port="3307",
    username="root",
    password="",
    database="saep"
)

def get_db():
    return conn