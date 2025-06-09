class Config:
    SECRET_KEY = ("dev",)
    JWT_SECRET_KEY = "super_secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///flaskr.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
