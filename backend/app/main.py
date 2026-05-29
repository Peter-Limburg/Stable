from fastapi import FastAPI
from app.routes import webhooks

app = FastAPI(title="Heimdall")

app.include_router(webhooks.router, prefix="/webhooks")
