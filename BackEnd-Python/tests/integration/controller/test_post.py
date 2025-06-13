from http import HTTPStatus
from src.models.Post import Post, db


def test_created_post(client, role_admin):
    # Given
    post = db.session.execute(db.select(Post).where(Post.post_id==1)).scalar()

    # When
    response = client.post(
        f"/posts/",
        json={
            "title": "Esse é o Titulo.",
            "body": "Esse é o corpo teste.",
            "author_id": 1,
        },
        headers={"Authorization": f"Bearer {role_admin}"},
    )

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
            "message": "Post criado!",
            "Title": post.title,
            "Body": post.body,
            "Created": post.created,
        }
