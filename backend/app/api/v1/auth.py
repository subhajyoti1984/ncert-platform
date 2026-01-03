from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.db import get_conn
from app.core.security import verify_password
import jwt
import datetime
import os

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

security = HTTPBearer()

SECRET = os.getenv("JWT_SECRET", "CHANGE_THIS")
ALGORITHM = "HS256"


# -------------------------
# LOGIN
# -------------------------
@router.post("/login")
def login(payload: dict):
    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    with get_conn.cursor() as cur:
        cur.execute(
            "SELECT id, password_hash FROM users WHERE email = %s",
            (email,)
        )
        row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_id, password_hash = row

    if not verify_password(password, password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {
            "sub": str(user_id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
        },
        SECRET,
        algorithm=ALGORITHM
    )

    return {"token": token}


# -------------------------
# CURRENT USER
# -------------------------
@router.get("/me")
def me(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET,
            algorithms=[ALGORITHM]
        )
        return {"user_id": payload["sub"]}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
