from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from ..models.User import User, db
from flask_bcrypt import bcrypt

app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = db.session.execute(db.select(User).where(User.username==username)).scalar()
    if not user or bcrypt.check_password_hash(user.password, password):
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED
    
    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token}
