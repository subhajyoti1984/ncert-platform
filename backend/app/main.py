from fastapi import FastAPI
from app.api.v1.learning import router as learning_router
from app.api.v1.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NCERT Learning Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

app.include_router(
    learning_router,
    prefix="/api/v1/learning"
)

@app.get("/")
def health():
    return {"status": "ok"}

