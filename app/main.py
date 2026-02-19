
from fastapi import FastAPI
from datetime import datetime, timezone
from contextlib import asynccontextmanager

from app.core.init_db import init_db
from app.api.webhook import router as webhook_router
from app.api.transaction import router as transaction_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Transaction Webhook Service",
    version="1.0.0",
    description="Service to receive and process transaction webhooks asynchronously",
    lifespan=lifespan
)

app.include_router(webhook_router)
app.include_router(transaction_router)


@app.get("/")
def health_check():
    return {
        "status": "HEALTHY",
        "current_time": datetime.now(timezone.utc).isoformat()
    }
