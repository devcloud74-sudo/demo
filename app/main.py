from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="Railway Demo API")


@app.get("/")
def home():
    returni {
        "message": "FastAPI app deployed successfully on Railway 🚀",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "local")
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }
