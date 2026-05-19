import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.diagnose import router as diagnose_router


app = FastAPI(
    title="FMDA",
    description="Family Medicine Doctor Assistant",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:8501")],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def root():
    return {
        "message": "FMDA is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


app.include_router(diagnose_router)
