import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("src.repository.config.Config")
    migrate = Migrate()
    jwt = JWTManager(app)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # from .controller.routes import post
    # app.register_blueprint(post.app)
    from .controller.routes import user
    app.register_blueprint(user.app)
    from .controller import auth
    app.register_blueprint(auth.app)
    
    from .controller.cli import register_comands
    register_comands(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
