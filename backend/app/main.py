from fastapi import FastAPI
from app.api.v1.learning import router as learning_router
from app.api.auth import router as auth_router

app = FastAPI(title="NCERT Learning Engine")

app.include_router(auth_router)

app.include_router(
    learning_router,
    prefix="/api/v1/learning"
)

@app.get("/")
def health():
    return {"status": "ok"}

