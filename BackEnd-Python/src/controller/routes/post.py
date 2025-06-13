from flask import Blueprint, request
from http import HTTPStatus
from ...models.Post import Post, db
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity
from ...untils import require_role

app = Blueprint("post", __name__, url_prefix="/posts")


def _created_posts(current_user):
    data = request.json
    post = Post(
        title=data["title"],
        body=data["body"],
        author_id=current_user
    )
    db.session.add(post)
    db.session.commit()
    return post


def _list_posts():
    query = db.select(Post)
    result = db.session.execute(query).scalars()
    return [
        {
            "Name": results.title,
            "email": results.body,
            "created": results.created,
            "author_id": results.author_id,
        }
        for results in result
    ]


def _get_post_by_id(post_id: int):
    post = db.get_or_404(Post, post_id)
    return {
        "id": post.id,
        "Title": post.title,
        "Body": post.body,
        "Created": post.created,
        "Author": post.author_id,
    }


def _update_post(post_id: int):
    post = db.get_or_404(Post, post_id)
    data = request.json

    mapper = inspect(Post)
    for colunm in mapper.attrs:
        if colunm.key in data:
            setattr(Post, colunm.key, data[colunm.key])
    db.session.commit()
    return {
        "id": data.id,
        "Modification": {
            "Body_before": post.body,
            "Body_after": data.body,
        },
    }


def _delete_post(post_id: int):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    return {"message": "Post deleted."}, HTTPStatus.NO_CONTENT


@app.route("/", methods=["GET", "POST"])
@jwt_required()
def post_and_list():
    if request.method == "POST":
        request.json
        current_user = get_jwt_identity()
        post = _created_posts(current_user)
        return {
            "message": "Post criado!",
            "Title": post.title,
            "Body": post.body,
            "Created": post.created,
        }, HTTPStatus.CREATED
    elif request.method == "GET":
        return {"message": _list_posts()}, HTTPStatus.OK
    else:
        return {"error": "Method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED


@app.route("/<int:post_id>", methods=["GET", "DELETE"])
@jwt_required()
@require_role("admin")
def update_and_delete(post_id):
    if request.method == "GET":
        return {"message": _get_post_by_id(post_id)}, HTTPStatus.OK
    elif request.method == "PATCH":
        return {"message": _update_post(post_id)}, HTTPStatus.OK
    elif request.method == "DELETE":
        return _delete_post(post_id)
    else:
        return {"error": "Method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED
