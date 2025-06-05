from flask import Blueprint, request, jsonify
from database.main import get_db
from database.models import User
from sqlalchemy.orm import Session

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    if not data or 'login' not in data or 'password' not in data:
        return jsonify({"error": "Login and password required"}), 400
    
    db: Session = next(get_db())
    user = db.query(User).filter(User.login == data['login']).first()
    
    if not user or user.password != data['password']:  # В реальном проекте сравнивать хеши!
        return jsonify({"authenticated": False}), 401
    
    return jsonify({
        "authenticated": True,
        "user": {
            "login": user.login,
            "email": user.email
        }
    }), 200