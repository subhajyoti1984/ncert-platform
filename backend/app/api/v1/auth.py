from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.db import get_conn
from app.core.security import verify_password, hash_password, get_current_user
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

@router.post("/bootstrap")
def bootstrap_admin():

    # 🔒 HARD STOP unless explicitly allowed
    if os.getenv("ALLOW_BOOTSTRAP") != "true":
        raise HTTPException(status_code=403, detail="Bootstrap disabled")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT NOW()
    )
    """)

    cur.execute("SELECT COUNT(*) FROM users WHERE is_admin = TRUE")
    admin_count = cur.fetchone()[0]

    if admin_count > 0:
        conn.close()
        return {"message": "Admin already exists"}

    from app.core.security import hash_password

    cur.execute(
        """
        INSERT INTO users (email, password_hash, is_admin)
        VALUES (%s, %s, TRUE)
        """,
        ("admin@ncert.local", hash_password("admin123"))
    )

    conn.commit()
    conn.close()

    return {"message": "Admin created"}

# -------------------------
# LOGIN
# -------------------------
@router.post("/login")
def login(payload: dict):
    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    with get_conn() as conn:
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
            "sub": str(user_id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
        },
        SECRET,
        algorithm=ALGORITHM
    )

    return {"token": token}

@router.post("/admin/change-password")
def change_admin_password(
    new_password: str,
    admin_id: str = Depends(get_current_user)
):
    conn = get_conn()
    cur = conn.cursor()

    from app.core.security import hash_password

    cur.execute(
        """
        UPDATE users
        SET password_hash = %s
        WHERE id = %s AND is_admin = TRUE
        """,
        (hash_password(new_password), admin_id)
    )

    conn.commit()
    conn.close()

    return {"status": "password updated"}

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
