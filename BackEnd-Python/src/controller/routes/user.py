from flask import Blueprint, request
from http import HTTPStatus
from ...models.User import User, db
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required

app = Blueprint("user", __name__, url_prefix="/users")


def _created_user():
    data = request.json
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()


def _list_user():
    query = db.select(User)
    result = db.session.execute(query).scalars()
    return [
        {
            "id": results.id,
            "Name": results.username,
            "email": results.email,
        }
        for results in result
    ]


def _get_user_by_id(user_id: int):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "Name": user.username,
    }


def _update_user(user_id: int):
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)
    for colunm in mapper.attrs:
        if colunm.key in data:
            setattr(user, colunm.key, data[colunm.key])
    db.session.commit()
    return {"id": user.id, "username": user.username}

def _delete_user(user_id: int):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT    

@app.route("/", methods=["GET", "POST"])
@jwt_required()
def handle_user():
    if request.method == "POST":
        _created_user()
        return {"message": "Usuario criado!"}, HTTPStatus.CREATED
    else:
        return {"message": _list_user()}, HTTPStatus.OK


@app.route("/<int:user_id>", methods=["GET", "PATCH", "DELETE"])
def get_user_by_id(user_id):
    if request.method == "GET":
        return {"message": _get_user_by_id(user_id)}, HTTPStatus.OK
    elif request.method == "PATCH":
        return {"message": _update_user(user_id)}, HTTPStatus.OK
    elif request.method == "DELETE":
        return _delete_user(user_id)
    else:
        return {"error": "Method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED
