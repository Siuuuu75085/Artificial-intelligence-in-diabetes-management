from flask_jwt_extended import jwt_required,get_jwt
from functools import wraps
from flask import jsonify
def role_required(*roles):
    def w(fn):
        @wraps(fn)
        @jwt_required()
        def d(*a,**k):
            if get_jwt()["role"] not in roles:
                return jsonify(error="Forbidden"),403
            return fn(*a,**k)
        return d
    return w
