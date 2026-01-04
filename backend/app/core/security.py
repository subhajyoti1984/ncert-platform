import bcrypt
import jwt
import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# -------------------------
# PASSWORD UTILS
# -------------------------

def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )

# -------------------------
# JWT AUTH
# -------------------------

SECRET = os.getenv("JWT_SECRET", "CHANGE_THIS")
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET,
            algorithms=[ALGORITHM]
        )
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
