from flask import Flask
from flask_cors import CORS
from auth.auth import auth_blueprint
from auth.reg import reg_blueprint
from database.main import init_db

app = Flask(__name__)
CORS(app)

# Инициализация БД
init_db()

# Регистрация blueprint'ов
app.register_blueprint(auth_blueprint, url_prefix='/api')
app.register_blueprint(reg_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return "Auth Service is running"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')