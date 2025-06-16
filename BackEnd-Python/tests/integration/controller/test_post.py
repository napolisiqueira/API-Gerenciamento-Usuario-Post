from http import HTTPStatus
from src.models.Post import Post, db


def test_created_post(client, role_admin):
    # Given
    response = client.post(
        f"/posts/",
        json={
            "title": "Esse é o Titulo.",
            "body": "Esse é o corpo teste.",
            "author_id": 1,
        },
        headers={"Authorization": f"Bearer {role_admin}"},
    )

    # When
    post = db.session.execute(db.select(Post).where(Post.post_id == 2)).scalar()

    # Then
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {
        "message": "Post criado com sucesso!",
        "post": {
            "id": post.post_id,
            "title": post.title,
            "body": post.body,
            "created": post.created.strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "author_id": post.author_id,
        },
    }


def test_created_post_403(client, role_normal):
    # Given
    response = client.post(
        f"/posts/",
        json={
            "title": "Esse é o Titulo.",
            "body": "Esse é o corpo teste.",
            "author_id": 1,
        },
        headers={"Authorization": f"Bearer {role_normal}"},
    )

    # When
    post = db.session.execute(db.select(Post).where(Post.post_id == 2)).scalar()

    # Then
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json == {"message": "User dont have permission."}


def test_list_post(client, role_admin):
    # Given
    post = db.session.execute(db.select(Post)).scalars().all()

    # When
    response = client.get(f"/posts/", headers={"Authorization": f"Bearer {role_admin}"})

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "message": [
            {
                "title": result.title,
                "body": result.body,
                "created": result.created.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                "author_id": result.author_id,
            }
            for result in post
        ]
    }


def test_list_post_403(client, role_normal):
    # Given
    post = db.session.execute(db.select(Post)).scalars().all()

    # When
    response = client.get(
        f"/posts/", headers={"Authorization": f"Bearer {role_normal}"}
    )

    # Then
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json == {"message": "User dont have permission."}


def test_list_post_401(client):
    # When
    response = client.get(f"/posts/")

    # Then
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_get_post_by_id(client, role_admin):
    post = db.session.execute(db.select(Post).where(Post.post_id == 1)).scalar()

    response = client.get(
        "/posts/1", headers={"Authorization": {f"Bearer {role_admin}"}}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "message": {
            "Author": post.author_id,
            "Body": post.body,
            "Created": post.created.strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "Title": post.title,
            "id": post.post_id,
        },
    }


def test_get_post_by_id_404(client, role_admin):
    response = client.get(
        "/posts/2", headers={"Authorization": {f"Bearer {role_admin}"}}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
