from flask import Blueprint, request, jsonify
from database.main import get_db
from database.models import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

reg_blueprint = Blueprint('reg', __name__)

@reg_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'login' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Login, email and password required"}), 400
    
    db: Session = next(get_db())
    print(data)
    user = User(login=data['login'], email=data['email'], password=data['password'])
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError as e:
        db.rollback()
        return jsonify({"error": "User with this login or email already exists"}), 400
    
    return jsonify({
        "registered": True,
        "user": {
            "login": user.login,
            "email": user.email
        }
    }), 201