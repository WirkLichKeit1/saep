import mysql.connector
from mysql.connector import Error
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

connection_url = os.getenv('CONN_URL')
parsed_url = urlparse(connection_url)

db_path = parsed_url.path or ""
if isinstance(db_path, bytes):
    db_path = db_path.decode('utf-8')
elif not isinstance(db_path, str):
    db_path = str(db_path)

config = {
    'host': parsed_url.hostname,
    'port': parsed_url.port or 3306,
    'user': parsed_url.username,
    'password': parsed_url.password,
    'database': db_path.lstrip('/') if db_path else "",
    'ssl_disabled': False,
}

def get_db():
    return mysql.connector.connect(**config)