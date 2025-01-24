'''

'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/auth', methods=['GET'])
def check():
    """
    Обрабатывает GET запрос и возвращает состояние сервера
    """
    return "Сервис работает стабильно", 200

@app.route('/auth', methods=['POST'])
def auth():
    '''
    Непосредственно произвести авторизацию.
    '''
    
    data = request.data
    print(request.json)
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    login: str = data.get('login')
    password: str = data.get('password')
    
    
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
    