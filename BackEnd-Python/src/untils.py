from functools import wraps
from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity
from src.models.User import User, db

def require_role(role_name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kargs):
            user_id = get_jwt_identity()
            user = db.get_or_404(User, user_id)

            if user.role.name != role_name:
                return {"message": "User dont have permission."}, HTTPStatus.FORBIDDEN
            return f(*args, **kargs)
        return wrapped
    return decorator

def eleva_quadrado(var):
    return var ** 2