from flask import Blueprint, request
from http import HTTPStatus
from ...models.Roles import Role, db
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required

app = Blueprint("role", __name__, url_prefix="/roles")


def _created_role():
    data = request.json
    role = Role(name=data["name"])
    db.session.add(role)
    db.session.commit()


def _list_roles():
    query = db.select(Role)
    result = db.session.execute(query).scalars()
    return [
        {
            "id": results.id,
            "Name": results.name,
        }
        for results in result
    ]


@app.route("/", methods=["GET", "POST"])
@jwt_required()
def create_role_route():
    if request.method == "POST":
        _created_role()
        return {"message": "Role criada!"}, HTTPStatus.CREATED
    else:
        return {"message": _list_roles()}, HTTPStatus.OK
