from fastapi import APIRouter, HTTPException
from app.core.db import conn
from app.core.security import verify_password
import jwt
import datetime
import os

router = APIRouter()

# NEVER hardcode in real deployments
SECRET = os.getenv("JWT_SECRET", "CHANGE_THIS")

# -------------------------
# LOGIN
# -------------------------
@router.post("/login")
def login(payload: dict):
    """
    Payload:
    {
      "email": "...",
      "password": "..."
    }
    """

    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    with conn.cursor() as cur:
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
            "user_id": str(user_id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
        },
        SECRET,
        algorithm="HS256"
    )

    return {"token": token}


# -------------------------
# CURRENT USER
# -------------------------
@router.get("/me")
def me(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {
            "user_id": payload["user_id"]
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
