import jwt
from fastapi import HTTPException

def require_user(token):
    try:
        return jwt.decode(token, "CHANGE_THIS", algorithms=["HS256"])
    except:
        raise HTTPException(401, "Unauthorized")
