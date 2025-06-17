from src.app import ma

class UserSchema(ma.Schema):
    class Meta:
        fileds = ("id", "username", "email", "role_id")