from fastapi import FastAPI
from app.api.v1.learning import router as learning_router

app = FastAPI(title="NCERT Learning Engine")

app.include_router(
    learning_router,
    prefix="/api/v1/learning"
)
