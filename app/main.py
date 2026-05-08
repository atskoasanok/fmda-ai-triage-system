from fastapi import FastAPI

from app.api.diagnose import router as diagnose_router


app = FastAPI(
    title="FMDA",
    description="Family Medicine Doctor Assistant",
    version="0.1.0"
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
