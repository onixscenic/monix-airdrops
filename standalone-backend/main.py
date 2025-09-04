from fastapi import FastAPI
from app.api import app as api_router

app = FastAPI(title="Monix Airdrops Backend")
app.mount("", api_router)
