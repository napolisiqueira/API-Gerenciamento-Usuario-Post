from http import HTTPStatus
from src.models.User import User, db
from src.models.Roles import Role


def test_get_user(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"message": {"id": user.id, "Name": user.username}}


def test_get_user_404(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user_id = 1

    response = client.get(f"/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_list_user(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    result = client.post(
        "auth/login", json={"username": user.username, "password": user.password}
    )
    access_token = result.json["access_token"]

    response = client.get(
        f"/users/", headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "message": [
            {
                "id": user.id,
                "Name": user.username,
                "email": user.email,
                "role": {
                    "id": user.role.id,
                    "name": user.role.name,
                },
            }
        ]
    }


def test_list_user_403(client):
    role = Role(name="normal")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    result = client.post(
        "auth/login", json={"username": user.username, "password": user.password}
    )
    access_token = result.json["access_token"]

    response = client.get(
        f"/users/", headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == HTTPStatus.FORBIDDEN


def test_list_user_401(client):
    role = Role(name="normal")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/")

    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_user(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    result = client.post(
        "auth/login", json={"username": user.username, "password": user.password}
    )
    access_token = result.json["access_token"]

    response = client.post(
        f"/users/",
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "username": "Create-Test",
            "password": "test",
            "email": "create@test.com",
            "role_id": role.id,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {"message": "Usuario criado!"}

def test_create_user_403(client):
    role = Role(name="normal")
    db.session.add(role)
    db.session.commit()

    user = User(
        username="Napoli-Test",
        password="test",
        email="napoli@test.com",
        role_id=role.id,
    )
    db.session.add(user)
    db.session.commit()

    result = client.post(
        "auth/login", json={"username": user.username, "password": user.password}
    )
    access_token = result.json["access_token"]

    response = client.post(
        f"/users/",
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "username": "Create-Test",
            "password": "test",
            "email": "create@test.com",
            "role_id": role.id,
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json ==  {"message": "User dont have permission."}