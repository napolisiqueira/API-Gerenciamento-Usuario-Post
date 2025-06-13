import pytest
from src.app import create_app
from src.extensions import db

@pytest.fixture(scope='function')
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
