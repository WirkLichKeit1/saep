from repositories.BaseRepository import get_db
from flask import Blueprint

db_bp = Blueprint("db", __name__)

@db_bp.route("/db", methods=["GET"])
def get_conn():
    return get_db()