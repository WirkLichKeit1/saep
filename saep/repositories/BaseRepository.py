import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    username="root",
    password="",
    database="saep"
)

def get_db():
    return conn