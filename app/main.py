"""meappai - minimal FastAPI app for CI/CD pipeline demo."""
import os
import time

from fastapi import FastAPI

app = FastAPI(title="meappai", version="0.1.0")
START = time.time()


@app.get("/")
def home():
    return {
        "app": "meappai",
        "version": "0.1.0",
        "message": "hello from meappai (CI/CD pipeline demo)",
        "uptime_s": round(time.time() - START, 1),
        "pod": os.environ.get("HOSTNAME", "unknown"),
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
