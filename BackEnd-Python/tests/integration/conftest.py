import pytest
from src.app import create_app
from src.extensions import db
from src.models.User import User
from src.models.Roles import Role


@pytest.fixture(scope="function")
def app():
    app = create_app(
        {
            "SECRET_KEY": "test",
            "JWT_SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "DEBUG": True,
        }
    )
    with app.app_context():
        db.create_all()
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def role_normal(client):
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
    return result.json["access_token"]


@pytest.fixture()
def role_admin(client):
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

    client.post(
        "/posts/", 
        json={"title": "Esse é o title fixture",
        "body": "Esse é o body fixture"},
        headers= {"Authorization": f"Bearer {result.json['access_token']}"},
    )

    return result.json["access_token"]

