from flask import Flask
from flask_cors import CORS
from controllers.authController import auth_bp
from controllers.dbController import db_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(db_bp)

if __name__ == "__main__":
    app.run()