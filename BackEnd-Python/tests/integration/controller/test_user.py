from http import HTTPStatus
from src.models.User import User, db
from src.models.Roles import Role
from sqlalchemy import func


def test_get_user(client, role_admin):
    # Given
    user = db.session.execute(db.select(User)).scalar()

    # When
    response = client.get(f"/users/{user.id}",  headers={"Authorization": f"Bearer {role_admin}"})

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"message": {"id": user.id, "Name": user.username}}


def test_get_user_404(client, role_admin):
    # Given
    user_id = 2

    # When
    response = client.get(f"/users/{user_id}",  headers={"Authorization": f"Bearer {role_admin}"})

    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_list_user(client, role_admin):
    # Given
    user = db.session.execute(db.select(User)).scalar()

    # When
    response = client.get(
        f"/users/", headers={"Authorization": f"Bearer {role_admin}"}
    )

    # Then
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


def test_list_user_403(client, role_normal):
    # When
    response = client.get(
        f"/users/", headers={"Authorization": f"Bearer {role_normal}"}
    )

    # Then
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json == {"message": "User dont have permission."}


def test_list_user_401(client):
    # When
    response = client.get(f"/users/")

    # Then
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_user(client, role_admin):
    # Given
    role_id = db.session.execute(db.select(Role.id).where(Role.name == "admin")).scalar()

    # When
    response = client.post(
        f"/users/",
        headers={"Authorization": f"Bearer {role_admin}"},
        json={
            "username": "Create-Test",
            "password": "test",
            "email": "create@test.com",
            "role_id": role_id,
        },
    )

    # Then
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {"message": "Usuario criado!"}
    assert db.session.execute(db.select(func.count(User.id))).scalar() == 2


def test_create_user_403(client, role_normal):
    # Given
    role_id = db.session.execute(
        db.select(Role.id).where(Role.name == "normal")
    ).scalar()

    # When
    response = client.post(
        f"/users/",
        headers={"Authorization": f"Bearer {role_normal}"},
        json={
            "username": "Create-Test",
            "password": "test",
            "email": "create@test.com",
            "role_id": role_id,
        },
    )

    #
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json == {"message": "User dont have permission."}
